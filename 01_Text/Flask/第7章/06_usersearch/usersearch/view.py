from flask import render_template, request, redirect
from usersearch import app, db
from usersearch.mst_user import mstUser

# '/users' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route("/users", methods=["GET"])
def users():
    # すべてのユーザーを取得
    mst_users = db.session.query(mstUser).all()
    # HTMLテンプレートをレンダリングしてデータを表示
    return render_template("user-list.html",users=mst_users)

# ①処理を追加
# ユーザー検索を行うルート
# @app.route("/users/search", methods=["GET"])
# 検索条件が空の場合、全ユーザーを取得
# idだけの場合、nameだけの場合、idとnameの3パターンで検索
