from flask import render_template, request, flash, redirect, url_for, session
from roomecho import db
from roomecho.member import member_bp
from roomecho.models.StayPlanMaster import StayPlanMaster
from roomecho.models.Booking import Booking
from roomecho.models.RoomMaster import RoomMaster
from roomecho.models.MemberMaster import MemberMaster
from datetime import date

# 予約追加ページ
@member_bp.route("/bookingadd", methods=["GET", "POST"])
@MemberMaster.is_login
def member_bookingadd():
    if request.method == "GET":

        # 検索条件を取得
        checkin_date = request.args.get("checkin_date")
        checkout_date = request.args.get("checkout_date")
        guest_count = request.args.get("guest_count")

        # 予約情報を取得
        stayplan = StayPlanMaster()
        stayplan.stayplan_id = request.args.get("stayplan_id")
        stayplan.stayplan_name = request.args.get("stayplan_name")
        price = request.args.get("price")

        # 予約追加ページを表示
        return render_template("bookingadd/member-booking-add.html",
            stayplan=stayplan,
            price=price,
            checkin_date=checkin_date,
            checkout_date=checkout_date,
            guest_count=guest_count
        )

    if request.method == "POST":

        # 検索条件を取得
        checkin_date = request.form.get("checkin_date")
        checkout_date = request.form.get("checkout_date")
        guest_count = request.form.get("guest_count")

        # 予約情報を取得
        stayplan_id = request.form.get("stayplan_id")
        stayplan = db.session.query(StayPlanMaster).get(stayplan_id)
        price = request.form.get("price")

        # ルーム情報を取得
        room = (
            db.session.query(RoomMaster)
            .filter(RoomMaster.roomtype_id == stayplan.roomtype_id)
            .first()
        )

        # ログイン中のユーザー情報を取得
        loginid = session.get("loginId")
        member = (
            db.session.query(MemberMaster).filter(MemberMaster.email == loginid).first()
        )

        # 予約データを生成
        booking = Booking(
            booking_datetime=date.today(),  # 予約日時
            room_no=room.room_no,  # 部屋番号
            stayplan_id=int(stayplan_id),  # 宿泊プランID
            member_id=member.user_id,  # 会員ID
            guest_count=int(guest_count),  # 宿泊人数
            price=int(price),  # 料金
            checkin_date=checkin_date,  # チェックイン日
            checkout_date=checkout_date,  # チェックアウト日
        )

        # 予約データをデータベースに保存
        db.session.add(booking)
        db.session.commit()

        # 予約完了ページを表示
        return render_template(
            "bookingadd/member-booking-add-comp.html",
            stayplan=stayplan,
            price=price,
            checkin_date=checkin_date,
            checkout_date=checkout_date,
            guest_count=guest_count
        )
