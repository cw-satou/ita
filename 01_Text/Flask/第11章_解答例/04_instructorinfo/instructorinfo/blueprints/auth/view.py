from flask import render_template, request, redirect, url_for, session
from . import auth_bp
from instructorinfo import db
from instructorinfo.models import StaffEntity

# ログイン処理
@auth_bp.route('login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # フォームからログインIDとパスワードを取得
        loginId = request.form['loginId']
        loginPassword = request.form['loginPassword']

        # データベースから該当するスタッフ情報を検索
        loginStaff = (
            db.session.query(StaffEntity)
            .filter(
                StaffEntity.login_id == loginId, 
                StaffEntity.login_password == loginPassword
            )
            .first()
        )

        # 認証成功時、セッションにスタッフ名を保存し、講師一覧ページへリダイレクト
        if loginStaff:
            session["staff_name"] = loginStaff.staff_name
            return redirect(url_for('instructors.show_inst_list'))
    
    # ログイン画面を表示
    return render_template('auth/staff-login.html')

# ログアウト処理
@auth_bp.route('logout')
def logout():
    session.pop('staff', None)  # セッションからスタッフ情報を削除
    return redirect(url_for('auth.login'))  # ログイン画面へリダイレクト
