from flask import render_template, request
from userlist import app, db
from userlist.mst_user import mstUser

# '/users' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/users', methods=['GET'])
def users():
    # すべてのユーザーデータを取得
    mst_users = db.session.query(mstUser).all()
    # ユーザーリストをHTMLテンプレートに渡して表示
    return render_template('user-list.html', users=mst_users)

# ①処理を追加
# 1件のユーザー詳細を表示するメソッド
# @app.route('/users/<id>', methods=['GET'])
# IDを指定して1つのアイテムを取得
