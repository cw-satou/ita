from flask import render_template, request, redirect, url_for
from userupdate import app, db
from userupdate.mst_user import mstUser

# '/users' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/users', methods=['GET'])
def users():
    # すべてのユーザーを取得
    mst_users = db.session.query(mstUser).all()
    # ユーザー一覧ページを表示
    return render_template('user-list.html', users=mst_users)

# '/users/edit/<id>' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/users/edit/<id>', methods=['GET'])
def users_edit(id):
    # IDでユーザーを取得
    mst_users = db.session.query(mstUser).get(id)
    # 編集用ページを表示
    return render_template('user-edit.html', user=mst_users)

# '/users/confirm' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/users/confirm', methods=['POST'])
def users_confirm():
    id = request.form['id']  # フォームからIDを取得
    name = request.form['name']  # フォームからユーザー名を取得
    email = request.form['email']  # フォームからメールアドレスを取得
    phone = request.form['phone']  # フォームから電話番号を取得

    # ユーザー情報を辞書にまとめる
    user = { 
        'id': id,
        'name': name,
        'email': email,
        'phone': phone,
    }
    # 確認ページを表示
    return render_template('user-confirm.html', user=user)

# '//users/update' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/users/update', methods=['POST'])
def users_update():
    id = request.form['id']  # フォームからIDを取得
    name = request.form['name']  # フォームからユーザー名を取得
    email = request.form['email']  # フォームからメールアドレスを取得
    phone = request.form['phone']  # フォームから電話番号を取得

    # 指定されたIDでユーザーを取得
    mst_user = db.session.query(mstUser).get(id)  # 主キーで検索
    if mst_user:  # 該当するユーザーデータが存在する場合
        mst_user.name = name  # ユーザー名を更新
        mst_user.email = email  # メールアドレスを更新
        mst_user.phone = phone  # 電話番号を更新
        db.session.commit()  # 変更をデータベースに保存

    # ユーザー一覧ページにリダイレクト
    return redirect(url_for('users'))
