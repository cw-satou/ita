from flask import render_template, request, redirect, url_for, session, get_flashed_messages
from . import instructors_bp
from instructorinfo import db
from instructorinfo.models import FieldEntity, InstEntity, is_login

# 講師一覧を表示するルート
@instructors_bp.route('inst')
@is_login  # ログインしているかを確認
def show_inst_list():
    # 講師情報と分野情報を取得し、講師IDの昇順で並び替え
    instList = (
        db.session.query(InstEntity, FieldEntity)
        .join(FieldEntity, InstEntity.field_id == FieldEntity.field_id)
        .order_by(InstEntity.instructor_id.asc())
        .all()
    )
    flash_messages = get_flashed_messages()  # フラッシュメッセージを取得
    return render_template('instructors/inst-list.html', instList=instList, messages=flash_messages, searchKey="全て表示")

# 講師を検索するルート
@instructors_bp.route('inst/search')
@is_login  # ログインしているかを確認
def search_inst():
    keyword = request.args.get('keyword', '').strip()  # 検索キーワードを取得し、前後の空白を除去
    # キーワードを含む経験を持つ講師情報を検索
    instList = (
        db.session.query(InstEntity, FieldEntity)
        .join(FieldEntity, InstEntity.field_id == FieldEntity.field_id)
        .filter(InstEntity.experience.like(f'%{keyword}%'))
        .order_by(InstEntity.instructor_id.asc())
        .all()
    )
    return render_template(
        'instructors/inst-list.html', 
        instList=instList, 
        searchKey=InstEntity.set_searchKey_text(keyword)  # 検索条件を設定
    )

# 新規講師登録画面を表示・登録処理
@instructors_bp.route('inst/create', methods=['GET', 'POST'])
@is_login  # ログインしているかを確認
def create_inst():
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
        return redirect(url_for('instructors.show_inst_list'))  # 一覧画面へリダイレクト
    return render_template('instructors/inst-regist.html', fieldList=fieldList)  # 登録画面を表示

# 講師登録をキャンセル（一覧画面へ戻る）
@instructors_bp.route('inst/cancel', methods=['POST'])
def cancel():
    return redirect(url_for('instructors.show_inst_list'))

# 講師情報の更新処理
@instructors_bp.route('inst/update/<int:instructor_id>', methods=['GET', 'POST'])
def update_inst(instructor_id):
    fieldList = db.session.query(FieldEntity).all()  # 分野一覧を取得
    if request.method == 'POST':
        # 該当する講師情報を取得し、更新
        entry = (
            db.session.query(InstEntity)
            .filter(InstEntity.instructor_id == instructor_id)
            .first()
        )
        entry.full_name = request.form['fullName']
        entry.business_name = request.form['businessName']
        entry.field_id = request.form['fieldId']
        entry.experience = request.form['experience']
        db.session.commit()  # 変更を保存
        return redirect(url_for('instructors.show_inst_list'))  # 一覧画面へリダイレクト

    # 更新対象の講師情報を取得
    entry = (
        db.session.query(InstEntity, FieldEntity)
        .join(FieldEntity, InstEntity.field_id == FieldEntity.field_id)
        .filter(InstEntity.instructor_id == instructor_id)
        .first()
    )
    return render_template('instructors/inst-update.html', instEntity=entry, fieldList=fieldList)  # 更新画面を表示

# 講師情報の削除処理
@instructors_bp.route('inst/delete/<int:instructor_id>', methods=['POST'])
def delete_inst(instructor_id):
    # 削除対象の講師情報を取得
    entry = (
        db.session.query(InstEntity)
        .filter(InstEntity.instructor_id == instructor_id)
        .first()
    )
    db.session.delete(entry)  # データベースから削除
    db.session.commit()  # 変更を保存
    return redirect(url_for('instructors.show_inst_list'))  # 一覧画面へリダイレクト
