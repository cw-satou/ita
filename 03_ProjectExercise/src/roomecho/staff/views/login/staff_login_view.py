import os
from flask import render_template, request, redirect, url_for, flash, session
from roomecho import db
from roomecho.staff import staff_bp
from roomecho.models.StaffMaster import StaffMaster

# スタッフサブシステムのログイン
# GET: ログイン画面の表示
# POST: ログインチェック処理
@staff_bp.route('/', methods=['GET', 'POST'])
def login():

    # POSTリクエストの場合、ログイン処理を行う
    if request.method == 'POST':
        loginId = request.form['loginId']
        loginPassword = request.form['loginPassword']

        # アカウント名が空の場合、エラーメッセージを表示
        if not loginId:
            err_message = "[アカウント名]を入力してください"
            return render_template("login/staff-login.html", err_message=err_message)

        # パスワードが空の場合、エラーメッセージを表示
        if not loginPassword:
            err_message = "[パスワード]を入力してください"
            return render_template("login/staff-login.html", err_message=err_message)

        # データベースからログイン情報を取得
        loginStaff = (
            db.session.query(StaffMaster)
            .filter(
                StaffMaster.account_name == loginId, 
                StaffMaster.password == loginPassword
            )
            .first()
        )

        # ログイン情報が正しい場合、セッションにユーザー情報を保存し、メニュー画面にリダイレクト
        if loginStaff:
            session["loginId"] = loginId
            session["staff_name"] = loginStaff.staff_name
            return redirect(url_for('staff.menu'))
        else:
            # ログイン情報が誤り、エラーメッセージを表示
            err_message = "[アカウント名]または[パスワード]が正しくありません" 
            return render_template("login/staff-login.html", err_message=err_message)

    # GETリクエストの場合、ログイン画面を表示
    return render_template("login/staff-login.html")


# スタッフサブシステムのログアウト
@staff_bp.route('/logout')
def logout():
    # セッションからユーザー情報を削除
    session.pop('loginId', None)
    session.pop('account_name', None)
    session.pop('division_name', None)
    session.pop('staff_name', None)

    # ログアウト完了画面を表示
    return render_template("login/staff-logout.html")
