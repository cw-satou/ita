from flask import render_template, flash, request, redirect, session, url_for
from sessionsample import app

# '/' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route("/", methods=["GET"])
def start():
    # 初期画面を表示
    return render_template("/session.html")

# '/setSession' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route("/setSession", methods=["GET"])
def setSession():
    # クエリパラメータ `name` を取得し、セッションに保存
    name = request.args.get('name')
    session['name'] = name

    # セッションに保存したことを伝えるメッセージを作成
    msg = "セッションに名前をセットしました: " + name
    return render_template("/session.html", message=msg)

# '/getSession' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route("/getSession", methods=["GET"])
def getSession():
    # セッションから `name` を取得
    name = session.get("name")

    # セッションにデータがあるかを確認し、メッセージを設定
    if not name:
        msg = "セッションにセットした名前がありません"
    else:
        msg = "セッションにセットした名前: " + name

    return render_template("/session.html", message=msg)

# '/invalidateSession' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route("/invalidateSession", methods=["GET"])
def invalidateSession():
    # セッションから `name` を削除
    session.pop("name", None)

    # セッションを無効化したことを伝えるメッセージを作成
    msg = "セッションを無効化しました"
    return render_template("/session.html", message=msg)
