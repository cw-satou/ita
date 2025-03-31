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

# '/users/<id>' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/users/<id>', methods=['GET'])
def users_id(id):
    # IDを指定してユーザーデータを取得
    mst_users = db.session.query(mstUser).get(id)
    # ユーザー詳細をHTMLテンプレートに渡して表示
    return render_template('user-detail.html', user=mst_users)
