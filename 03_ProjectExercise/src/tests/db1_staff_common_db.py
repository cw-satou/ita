# testsディレクトリのスクリプトでroomechoのスクリプトをインポートするための設定
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(src_dir)

# インポート
from roomecho import app, db
from roomecho.models.StaffMaster import StaffMaster
from roomecho.models.MemberMaster import MemberMaster
from roomecho.models.RoomMaster import RoomMaster
from roomecho.models.RoomTypeMaster import RoomTypeMaster
from roomecho.models.Booking import Booking
from roomecho.models.StayPlanMaster import StayPlanMaster
from datetime import date

with app.app_context():

    db.drop_all()
    db.create_all()

    # 会員情報を作成
    members = [
        MemberMaster( 
            member_name='会員一郎', 
            address='東京都新宿区１－１', 
            phone_number='09011111111', 
            email='kaiin1@example.com', 
            password='pass001'
        ),
        MemberMaster( 
            member_name='会員二子', 
            address='東京都新宿区１－２', 
            phone_number='09022222222', 
            email='kaiin2@example.com', 
            password='pass002'
        ),
    ]

    # データベースに追加
    db.session.bulk_save_objects(members)
    db.session.commit()

    # 客室タイプデータを作成
    room_types = [
        RoomTypeMaster(
            roomtype_name="ダブル",
            roomtype_price=10000,
            roomtype_image_filename="double.jpg",
            roomtype_description="客室にかんする説明",
            roomtype_facilities="設備１、備品１",
            maximum_capacity=2
        ),
    ]

    # データベースに追加
    db.session.add_all(room_types)
    db.session.commit()

    # 客室データを作成
    rooms = [
        RoomMaster(
            room_no="101", 
            roomtype_id=1
        ),
    ]

    # データベースに追加
    db.session.add_all(rooms)
    db.session.commit()

    # 宿泊プランを作成
    stay_plans = [
        StayPlanMaster(
            stayplan_name="宿泊プラン１",
            stayplan_description="ベーシックプラン",
            roomtype_id=1,
            additional_charges=1000,
            stayplan_start_from=date(2025, 1, 1),
            stayplan_end_of=date(2025, 12, 31),
        ),
    ]

    # データベースに追加
    db.session.add_all(stay_plans)
    db.session.commit()

    # 予約データを作成
    bookings = [
        Booking(
            booking_datetime = date(2025, 7, 1),
            member_id=1,
            room_no="101",
            stayplan_id=1,
            guest_count=2,
            price=100000,
            checkin_date=date(2025, 8, 1),
            checkout_date=date(2025, 8, 3),
        ),
        Booking(
            booking_datetime = date(2025, 1, 1),
            member_id=2,
            room_no="101",
            stayplan_id=1,
            guest_count=2,
            price=100000,
            checkin_date=date(2025, 4, 1),
            checkout_date=date(2025, 4, 3),
        ),
    ]

    # データベースに追加
    db.session.add_all(bookings)
    db.session.commit()

    # スタッフ情報を作成
    staffs = [
        StaffMaster( 
            account_name='staff1', 
            staff_name='スタッフ１', 
            division_name='マネージャー', 
            password='staff1'
        ),
    ]

    # データベースに追加
    db.session.bulk_save_objects(staffs)
    db.session.commit()

    print("Database initialized.")
