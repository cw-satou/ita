from flask import render_template, request, redirect, url_for, session, get_flashed_messages
from instructorinfo import app, db
from .models import FieldEntity, InstEntity, StaffEntity, is_login

# スタッフのログイン処理
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # フォームからログインIDとパスワードを取得
        loginId = request.form['loginId']
        loginPassword = request.form['loginPassword']

        # データベースから該当するスタッフ情報を検索
        loginStaff = (
            db.session.query(StaffEntity)
            .filter(
                StaffEntity.login_id == loginId, 
                StaffEntity.login_password == loginPassword
            )
            .first()
        )

        # ログイン成功時、セッションにスタッフ名を保存し、一覧画面へリダイレクト
        if loginStaff:
            session["staff_name"] = loginStaff.staff_name
            return redirect(url_for('showInstList'))
    
    # ログイン画面を表示
    return render_template('staff-login.html')

# ログアウト処理
@app.route('/logout')
def logout():
    session.pop('staff', None)  # セッションからスタッフ情報を削除
    return redirect(url_for('login'))  # ログイン画面へリダイレクト

# 講師一覧を表示
@app.route('/inst')
@is_login  # ログイン認証を適用
def showInstList():
    # 講師情報と分野情報を取得し、講師IDの昇順で並び替え
    instList = (
        db.session.query(InstEntity, FieldEntity)
        .join(FieldEntity, InstEntity.field_id == FieldEntity.field_id)
        .order_by(InstEntity.instructor_id.asc())
        .all()
    )
    flash_messages = get_flashed_messages()  # フラッシュメッセージを取得
    return render_template('inst-list.html', instList=instList, messages=flash_messages, searchKey="全て表示")

# 講師情報を検索
@app.route('/inst/search')
@is_login  # ログイン認証を適用
def searchInst():
    keyword = request.args.get('keyword', '').strip()  # 検索キーワードを取得し、空白を除去
    # キーワードを含む経験を持つ講師情報を検索
    instList = (
        db.session.query(InstEntity, FieldEntity)
        .join(FieldEntity, InstEntity.field_id == FieldEntity.field_id)
        .filter(InstEntity.experience.like(f'%{keyword}%'))
        .order_by(InstEntity.instructor_id.asc())
        .all()
    )
    return render_template(
        'inst-list.html', 
        instList=instList, 
        searchKey=InstEntity.set_searchKey_text(keyword)  # 検索条件を設定
    )

# 講師情報を新規登録
@app.route('/inst/create', methods=['GET', 'POST'])
@is_login  # ログイン認証を適用
def createInst():
    fieldList = db.session.query(FieldEntity).all()  # 分野一覧を取得
    if request.method == 'POST':
        # フォームから送信されたデータを取得し、講師情報を作成
        entry = InstEntity(
            full_name=request.form['fullName'],
            business_name=request.form['businessName'],
            field_id=request.form['fieldId'],
            experience=request.form['experience']
        )
        db.session.add(entry)  # データベースに追加
        db.session.commit()  # 変更を保存
        return redirect(url_for('showInstList'))  # 一覧画面へリダイレクト
    return render_template('inst-regist.html', fieldList=fieldList)  # 登録画面を表示

# 登録処理をキャンセル（一覧画面へ戻る）
@app.route('/inst/cancel', methods=['POST'])
def cancel():
    return redirect(url_for('showInstList'))

# 講師情報を更新
@app.route('/inst/update/<int:instructor_id>', methods=['GET', 'POST'])
def updateInst(instructor_id):
    fieldList = db.session.query(FieldEntity).all()  # 分野一覧を取得
    if request.method == 'POST':
        # 該当する講師情報を検索し、データを更新
        entry = (
            db.session.query(InstEntity)
            .filter(InstEntity.instructor_id == instructor_id)
            .first()
        )
        entry.full_name=request.form['fullName']
        entry.business_name=request.form['businessName']
        entry.field_id=request.form['fieldId']
        entry.experience=request.form['experience']
        db.session.commit()  # 変更を保存
        return redirect(url_for('showInstList'))  # 一覧画面へリダイレクト

    # 更新対象の講師情報を取得
    entry = (
        db.session.query(InstEntity, FieldEntity)
        .join(FieldEntity, InstEntity.field_id == FieldEntity.field_id)
        .filter(InstEntity.instructor_id == instructor_id)
        .first()
    )
    return render_template('inst-update.html', instEntity=entry, fieldList=fieldList)  # 更新画面を表示

# 講師情報を削除
@app.route('/inst/delete/<int:instructor_id>', methods=['POST'])
def deleteInst(instructor_id):
    # 削除対象の講師情報を取得
    entry = (
        db.session.query(InstEntity)
        .filter(InstEntity.instructor_id == instructor_id)
        .first()
    )
    db.session.delete(entry)  # データベースから削除
    db.session.commit()  # 変更を保存
    return redirect(url_for('showInstList'))  # 一覧画面へリダイレクト
