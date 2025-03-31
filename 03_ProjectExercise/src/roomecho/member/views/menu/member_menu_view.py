import os
from flask import render_template, request, redirect, url_for, flash, session
from roomecho import db
from roomecho.member import member_bp
from roomecho.models.MemberMaster import MemberMaster


# メンバーのメニューページ
@member_bp.route("/menu", methods=["GET", "POST"])
@MemberMaster.is_login
def menu():
    # データベースからログインIDに一致するメンバー情報を取得
    loginMember = (
        db.session.query(MemberMaster)
            .filter(MemberMaster.email == session.get("loginId"))
            .first()
    )

    # ログインIDがデータベースに存在しない場合、ログインページにリダイレクト
    if not loginMember:
        return redirect(url_for("member.login"))

    # メニューページを表示
    return render_template("menu/member-menu.html", member=loginMember)
