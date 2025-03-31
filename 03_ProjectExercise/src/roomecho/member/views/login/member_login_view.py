from flask import render_template, request, flash, redirect, url_for, session
from roomecho import db
from roomecho.member import member_bp
from roomecho.models.MemberMaster import MemberMaster

# 会員ログインページ
@member_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # ログインフォームからメールアドレスとパスワードを取得
        loginId = request.form['loginId']
        loginPassword = request.form['loginPassword']

        # メールアドレスが空の場合
        if not loginId:
            err_message = "[メールアドレス]を入力してください"
            return render_template("login/member-login.html", err_message=err_message)

        # パスワードが空の場合
        if not loginPassword:
            err_message = "[パスワード]を入力してください"
            return render_template("login/member-login.html", err_message=err_message)

        # データベースからログイン情報を取得
        loginMember = (
            db.session.query(MemberMaster)
            .filter(
                MemberMaster.email == loginId, 
                MemberMaster.password == loginPassword
            )
            .first()
        )

        # ログイン情報が正しい場合
        if loginMember:
            # セッションにログインIDと会員名を保存
            session["loginId"] = loginId
            session["member_name"] = loginMember.member_name
            # メニュー画面にリダイレクト
            return redirect(url_for('member.menu'))
        else:
            # ログイン情報が誤り、エラーメッセージを表示
            err_message = "[メールアドレス]または[パスワード]が正しくありません" 
            return render_template("login/member-login.html", err_message=err_message)

    # ログインページを表示
    return render_template("login/member-login.html")

# 会員ログアウト機能
@member_bp.route('/logout')
def logout():
    # セッションからログイン情報を削除
    session.pop('loginId', None)
    session.pop('member_name', None)
    # ログアウト完了ページを表示
    return render_template("login/member-logout.html")
