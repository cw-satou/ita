from flask import render_template, request, redirect, url_for
from userdelete import app, db
from userdelete.mst_user import mstUser

# '/users' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/users', methods=['GET'])
def users():
    # すべてのユーザーデータを取得
    mst_users = db.session.query(mstUser).all()
    # ユーザー一覧ページを表示
    return render_template('user-list.html', users=mst_users)

# '/users/<id>' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/users/<id>', methods=['GET'])
def users_confirm(id):
    # 指定されたIDのユーザー情報を取得
    mst_users = db.session.query(mstUser).get(id)
    # ユーザー削除確認ページを表示
    return render_template('user-confirm.html', user=mst_users)

# '/users/delete' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/users/delete', methods=['POST'])
def users_delete():
    id = request.form['id']  # フォームからユーザーIDを取得

    # 指定されたIDのユーザーを取得
    mst_user = db.session.query(mstUser).get(id)
    if mst_user:  # 該当するユーザーが存在する場合
        # ユーザーをデータベースから削除
        db.session.delete(mst_user)
        # 変更をデータベースに反映
        db.session.commit()

    # ユーザー一覧ページにリダイレクト
    return redirect(url_for('users'))
