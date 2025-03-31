from flask import render_template, request, redirect
from introduction import app

# アプリケーションのルートパスを取得（デフォルトは "/"）
application_root = app.config.get("APPLICATION_ROOT", "/")

# リクエストが処理される前に実行される処理
@app.before_request
def set_script_name():
    # 環境変数にアプリのルートパスを設定
    request.environ["SCRIPT_NAME"] = application_root

# ルート（"/"）にアクセスしたときの処理
@app.route("/")
def redirect_root():
    # アプリケーションのルートへリダイレクト
    return redirect(application_root + "/")

# 一覧ページを表示
@app.route(f"{application_root}/")
def show_list():
    return render_template('list.html')

# 登録ページを表示（POSTメソッドのみ許可）
@app.route(f"{application_root}/regist", methods=['POST'])
def show_regist():
    return render_template('regist.html')
