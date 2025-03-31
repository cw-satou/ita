from flask import render_template, request, redirect
from userdelete import app, db
from userdelete.mst_user import mstUser

# '/users' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/users', methods=['GET'])
def users():
    # ユーザーデータを取得
    mst_users = db.session.query(mstUser).all()
    # ユーザー情報を渡してレンダリング
    return render_template('user-list.html', users=mst_users)

# '/users/<id>' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/users/<id>', methods=['GET'])
def users_confirm(id):
    # ユーザーIDでユーザーデータを取得
    mst_users = db.session.query(mstUser).get(id)
    # 'ユーザー情報を渡してレンダリング
    return render_template('user-confirm.html', user=mst_users)

# ① ユーザを削除する処理
# 削除を実施し一覧表示
# @app.route('/users/delete', methods=['POST'])
