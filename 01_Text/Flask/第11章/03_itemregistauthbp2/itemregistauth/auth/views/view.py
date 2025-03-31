import os
from flask import render_template, request, redirect, url_for, flash, session
from itemregistauth import db
from itemregistauth.auth import auth_bp
from itemregistauth.auth.models.mst_accounts import Mst_account

# "/login" にアクセスしたときの処理（ログイン画面の表示）
@auth_bp.route("login", methods=["GET"])
def login():
    return render_template("login.html")

# "/login" にアクセスしたときの処理（ログイン処理の実行）
@auth_bp.route("login", methods=["POST"])
def login_exec():
    # ログインエラー判定用の変数
    isLoginError = False

    # フォームからユーザーIDとパスワードを取得
    user_id = request.form['user_id']
    password = request.form['password']

    # ユーザーIDの入力チェック
    if not user_id:
        isLoginError = True
        flash("{arg1}は必須入力項目です。".format(arg1='ユーザID'))

    # パスワードの入力チェック
    if not password:
        isLoginError = True
        flash("{arg1}は必須入力項目です。".format(arg1='パスワード'))

    # データベースから該当ユーザーを検索
    mst_account = db.session.query(Mst_account).filter(
        Mst_account.user_id == user_id,
        Mst_account.password == password,
    ).first()

    # 一致するアカウントがない場合、エラーメッセージを表示
    if not mst_account:
        isLoginError = True
        flash("「user_id」と「password」が一致しません。")

    # エラーがある場合はログイン画面へリダイレクト
    if isLoginError:
        return redirect(url_for('auth.login'))

    # ログイン成功時、ユーザーIDをセッションに保存
    session["loggedInUser"] = mst_account.user_id

    # 商品入力画面へリダイレクト
    return redirect(url_for('items.input'))

# "/logout" にアクセスしたときの処理（ログアウト処理）
@auth_bp.route("logout", methods=["GET"])
def logout():
    # セッションからログイン情報を削除
    session.pop('loggedInUser', None)

    # ログイン画面へリダイレクト
    return redirect(url_for('auth.login'))
