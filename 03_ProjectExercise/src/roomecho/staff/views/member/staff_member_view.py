import re
from flask import render_template, request, redirect, url_for, flash, session
from datetime import datetime
from roomecho import db
from roomecho.staff import staff_bp
from roomecho.models.MemberMaster import MemberMaster
from roomecho.models.StaffMaster import StaffMaster
from roomecho.models.Booking import Booking


# 会員一覧画面
@staff_bp.route("/member", methods=["GET"])
@StaffMaster.is_login
def member_list():
    # 会員情報をデータベースから取得し、ユーザーID順に並べる
    members = db.session.query(MemberMaster).order_by("user_id").all()
    # 会員一覧画面を表示
    return render_template("member/staff-member-list.html", members=members)


# 会員情報変更画面
@staff_bp.route("/member/<user_id>/edit", methods=["GET", "POST"])
@StaffMaster.is_login
def member_edit(user_id):

    if request.method == "GET":
        # 指定されたユーザーIDの会員情報を取得
        member = db.session.query(MemberMaster).get(user_id)
        # 会員情報編集画面を表示
        return render_template("member/staff-member-edit.html", member=member)

    if request.method == "POST":
        # エラーフラグ、エラーメッセージを初期化
        err_flag = False
        err_member_name = ""
        err_address = ""
        err_phone_number = ""
        err_email = ""

        # 会員名の入力チェック
        if not request.form["member_name"]:
            err_flag = True
            err_member_name = "[会員名]を入力してください"
        elif len(request.form["member_name"]) > 30:
            err_flag = True
            err_member_name = "[会員名]は30文字以内で入力してください"

        # メールアドレスの入力チェック
        if not request.form["email"]:
            err_flag = True
            err_email = "[メールアドレス]を入力してください"
        elif len(request.form["email"]) > 254:
            err_flag = True
            err_email = "[メールアドレス]は254文字以内で入力してください"
        elif not re.match(
            r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", request.form["email"]
        ):
            err_flag = True
            err_email = "[メールアドレス]はメールアドレスの形式で入力してください"

        # 電話番号の入力チェック
        if not request.form["phone_number"]:
            err_flag = True
            err_phone_number = "[電話番号]を入力してください"
        elif (
            len(request.form["phone_number"]) < 10
            or len(request.form["phone_number"]) > 11
        ):
            err_flag = True
            err_phone_number = "[電話番号]は10文字～11文字以内で入力してください"

        # 住所の入力チェック
        if not request.form["address"]:
            err_flag = True
            err_address = "[住所]を入力してください"
        elif len(request.form["address"]) > 254:
            err_flag = True
            err_address = "[住所]は254文字以内で入力してください"

        # エラーがあった場合、編集画面に戻す
        if err_flag:
            # 一時的にMemberMasterオブジェクトを作成してフォームデータを保持
            member = MemberMaster()
            member.user_id = user_id
            member.member_name = request.form["member_name"]
            member.phone_number = request.form["phone_number"]
            member.address = request.form["address"]
            member.email = request.form["email"]

            # エラーメッセージとともに編集画面を表示
            return render_template(
                "member/staff-member-edit.html",
                member=member,
                err_member_name=err_member_name,
                err_address=err_address,
                err_phone_number=err_phone_number,
                err_email=err_email,
            )

        # エラーがなければ、データベースを更新
        member = db.session.query(MemberMaster).get(user_id)
        if member:
            member.member_name = request.form["member_name"]
            member.address = request.form["address"]
            member.phone_number = request.form["phone_number"]
            member.email = request.form["email"]
            db.session.commit()

        # 更新完了画面を表示
        return render_template("member/staff-member-edit-comp.html", member=member)


# 会員退会確認画面
@staff_bp.route("/member/<user_id>/del", methods=["GET", "POST"])
@StaffMaster.is_login
def member_del(user_id):

    # 指定されたユーザーIDの会員情報を取得
    member = db.session.query(MemberMaster).get(user_id)

    # 削除対象の有効な予約情報の研修を取得
    booking_count = (
        db.session.query(Booking).filter(
            Booking.member_id == user_id,
            Booking.checkout_date >= datetime.now()
        ).count()
    )
    
    if request.method == "GET":
        # 予約のある会員は退会できない
        if booking_count > 0:
            return render_template(
                "member/staff-member-del.html",
                member=member,
                err_message="予約情報のある会員は退会できません",
            )

        # 退会確認画面を表示
        return render_template("member/staff-member-del.html", member=member)

    if request.method == "POST":
        # 該当するレコードがあればデータベースから削除
        if member and booking_count == 0:
            db.session.delete(member)
            db.session.commit()

        # 退会完了画面を表示
        return render_template("member/staff-member-del-comp.html", member=member)
