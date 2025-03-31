from flask import render_template, request, flash, redirect, url_for, session
from roomecho import db
from roomecho.member import member_bp
from roomecho.models.StayPlanMaster import StayPlanMaster
from roomecho.models.RoomTypeMaster import RoomTypeMaster
from roomecho.models.RoomMaster import RoomMaster
from roomecho.models.Booking import Booking
from roomecho.models.MemberMaster import MemberMaster
from sqlalchemy import or_


# 空室検索ページを表示
@member_bp.route("/vacancy", methods=["GET"])
@MemberMaster.is_login
def member_vacancy_list():
    # 宿泊人数のドロップダウンの選択肢（リスト型）
    guest_counts = [1, 2, 3, 4]

    # 検索条件を初期化
    booking = Booking

    # 空室検索ページを表示
    return render_template(
        "vacancy/member-vacancy-list.html",
        booking=booking,
        guest_counts=guest_counts,
        err_flag=False,
    )


# 検索実行、プラン一覧を表示
@member_bp.route("/plans", methods=["GET", "POST"])
@MemberMaster.is_login
def member_plan_list():

    # 宿泊人数のドロップダウンの選択肢（リスト型）
    guest_counts = [1, 2, 3, 4]

    # リクエストメソッドに応じてパラメータを取得
    if request.method == "GET":
        checkin_date = request.args.get("checkin_date")
        checkout_date = request.args.get("checkout_date")
        guest_count = request.args.get("guest_count")
    else:
        checkin_date = request.form.get("checkin_date")
        checkout_date = request.form.get("checkout_date")
        guest_count = request.form.get("guest_count")

    # 画面のドロップダウンの初期選択状態を入力された宿泊人数にする
    if guest_count:
        selected_guest_count = int(guest_count)
    else:
        selected_guest_count = 0

    # 入力値を予約情報にセット
    booking = Booking
    booking.checkin_date = checkin_date
    booking.checkout_date = checkout_date
    booking.guest_count = guest_count

    # エラーチェック結果を初期化
    err_flag = False
    err_checkin_date = ""
    err_checkout_date = ""
    err_guest_count = ""

    # 必須項目のバリデーション
    if not checkin_date:
        err_flag = True
        err_checkin_date = "[チェックイン日]を入力してください"

    if not checkout_date:
        err_flag = True
        err_checkout_date = "[チェックアウト日]を入力してください"

    if guest_count == "0":
        err_flag = True
        err_guest_count = "[宿泊人数]を選択してください"
    else:
        guest_count = int(guest_count)

    # エラーがあったら入力画面に戻る
    if err_flag:
        return render_template(
            "vacancy/member-vacancy-list.html",
            booking=booking,
            guest_counts=guest_counts,
            err_checkin_date=err_checkin_date,
            err_checkout_date=err_checkout_date,
            err_guest_count=err_guest_count,
        )

    # 宿泊可能な宿泊プランの一覧データを作成する
    # 宿泊プランを初期化
    plans = []

    # 宿泊可能な客室タイプを検索
    # 条件: 客室タイプの宿泊人数が、入力された宿泊人数以上であること
    roomtypes = (
        db.session.query(RoomTypeMaster)
        .filter(RoomTypeMaster.maximum_capacity >= guest_count)
        .all()
    )

    # 宿泊可能な客室タイプが見つからない場合のエラーメッセージ
    if not roomtypes:
        return render_template(
            "vacancy/member-vacancy-list.html",
            err_message="宿泊プランが見つかりませんでした（定員オーバー）",
            booking=booking,
            guest_counts=guest_counts,
            selected_guest_count=selected_guest_count,
        )

    # 客室タイプごとの宿泊プランを検索
    for roomtype in roomtypes:
        print(roomtype)

        # 宿泊可能なプランを初期化
        plan = []

        # 宿泊プランを検索（期間内のプランを取得）
        stayplans = (
            db.session.query(StayPlanMaster)
            .filter(
                StayPlanMaster.stayplan_start_from <= checkin_date,
                StayPlanMaster.stayplan_end_of >= checkout_date,
                StayPlanMaster.roomtype_id == roomtype.roomtype_id,
            )
            .all()
        )

        # 予約データをチェック（期間が重なる他の予約がないか）
        for stayplan in stayplans:
            # 該当する room_no のリストを取得
            rooms = (
                db.session.query(RoomMaster)
                .filter(
                    RoomMaster.roomtype_id == roomtype.roomtype_id,
                    RoomMaster.roomtype_id == stayplan.roomtype_id,
                )
                .all()
            )

            for room in rooms:
                # 該当部屋の予約状況を確認
                existing_booking = (
                    db.session.query(Booking)
                    .filter(
                        Booking.stayplan_id == stayplan.stayplan_id,
                        Booking.room_no == room.room_no,  # 部屋番号が一致
                        or_(
                            Booking.checkin_date <= checkout_date,
                            Booking.checkout_date <= checkin_date,
                        ),
                    )
                    .first()
                )

                # 宿泊期間が重なる予約がない場合は予約可能
                if not existing_booking:
                    price = roomtype.roomtype_price + stayplan.additional_charges
                    plan.append((stayplan, price))

        if plan:
            plans.append((roomtype, plan))

    if not plans:
        # 空室がない場合のエラーメッセージ
        return render_template(
            "vacancy/member-vacancy-list.html",
            err_message="宿泊プランが見つかりませんでした（空室なし）",
            booking=booking,
            checkin_date=checkin_date,
            checkout_date=checkout_date,
            guest_count=guest_count,
            guest_counts=guest_counts,
            selected_guest_count=selected_guest_count,
        )

    # 該当条件で検索して、LIST表示
    return render_template(
        "vacancy/member-plan-list.html",
        checkin_date=checkin_date,
        checkout_date=checkout_date,
        guest_count=guest_count,
        guest_counts=guest_counts,
        selected_guest_count=selected_guest_count,
        plans=plans,
    )


# プラン詳細を表示
@member_bp.route("/plan/<stayplan_id>", methods=["GET"])
@MemberMaster.is_login
def member_plan(stayplan_id):

    # 引数を取得
    checkin_date = request.args.get("checkin_date")
    checkout_date = request.args.get("checkout_date")
    guest_count = request.args.get("guest_count")

    # 宿泊プランを取得
    stayplan = db.session.query(StayPlanMaster).get(stayplan_id)

    # 宿泊プランに紐づくルームタイプを取得
    roomtype = (
        db.session.query(RoomTypeMaster)
        .filter(RoomTypeMaster.roomtype_id == stayplan.roomtype_id)
        .first()
    )

    # 価格を計算
    price = roomtype.roomtype_price + stayplan.additional_charges

    # プラン詳細ページを表示
    return render_template(
        "vacancy/member-plan.html",
        checkin_date=checkin_date,
        checkout_date=checkout_date,
        guest_count=guest_count,
        stayplan=stayplan,
        roomtype=roomtype,
        price=price,
    )
