import os
from flask import render_template, request, redirect, url_for, flash, session
from roomecho import db
from roomecho.staff import staff_bp
from roomecho.models.StaffMaster import StaffMaster

# スタッフサブシステムのメニュー画面
@staff_bp.route('/menu', methods=['GET', 'POST'])
@StaffMaster.is_login
def menu():
    # セッションからアカウント名を取得
    session_login_id = session.get("loginId")
    session_staff_name = session.get("staff_name")

    # セッションにアカウント名が保存されていない場合、ログアウトページにリダイレクト
    if not session_login_id:
        return redirect(url_for('staff.logout'))

    # データベースからアカウント名に一致するスタッフ情報を取得
    loginStaff = (
        db.session.query(StaffMaster)
        .filter(StaffMaster.account_name == session_login_id)
        .first()
    )

    # アカウント名がデータベースに存在しない場合、ログアウトページにリダイレクト
    if not loginStaff:
        return redirect(url_for('staff.logout'))

    # メニューページを表示
    return render_template("menu/staff-menu.html")
