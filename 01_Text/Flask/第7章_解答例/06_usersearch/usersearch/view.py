from flask import render_template, request
from usersearch import app, db
from usersearch.mst_user import mstUser

# '/users' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/users', methods=['GET'])
def users():
    # すべてのユーザーを取得
    mst_users = db.session.query(mstUser).all()
    # ユーザーリストをHTMLテンプレートで表示
    return render_template('user-list.html', users=mst_users)

# '/users/search' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/users/search', methods=['GET'])
def users_search():
    # クエリパラメータから検索条件（IDと名前）を取得
    id = request.args.get('id')  # IDの取得
    name = request.args.get('name')  # 名前の取得

    # 検索条件がない場合、すべてのユーザーを取得
    if not id and not name:
        mst_users = db.session.query(mstUser).all()  # 全ユーザーを取得
    elif id and not name:
        # IDが指定されている場合、そのIDのユーザーのみ取得
        mst_users = db.session.query(mstUser).filter(
            mstUser.id == id  # IDが完全一致
        ).all()
    elif not id and name:
        # 名前が指定されている場合、部分一致で検索
        mst_users = db.session.query(mstUser).filter(
            mstUser.name.like(f'%{name}%')  # 名前が部分一致
        ).all()

    # 検索結果をHTMLテンプレートで表示
    return render_template('user-list.html', users=mst_users)
