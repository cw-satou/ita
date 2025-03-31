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

    # 会員データを作成
    members = [
        MemberMaster(
            member_name="山田　次郎",
            address="東京都渋谷区123-4-5",
            phone_number="09012345678",
            email="jiro.yamada@example.com",
            password="pass1234",
        ),
        MemberMaster(
            member_name="鈴木　花子",
            address="大阪府中央区難波456-7-8",
            phone_number="08087654321",
            email="hanako.suzuki@example.com",
            password="pass1234",
        ),
        MemberMaster(
            member_name="田中　史郎",
            address="京都府伏見区678-9",
            phone_number="07011223344",
            email="shiro.tanaka@example.com",
            password="pass1234",
        ),
        MemberMaster(
            member_name="中村　仁志",
            address="北海道札幌市98-75",
            phone_number="09099887766",
            email="hitoshi.nakamura@example.com",
            password="pass1234",
        ),
        MemberMaster(
            member_name="小林　有希",
            address="福岡県博多区321-95",
            phone_number="08066778899",
            email="yuki.kobayashi@example.com",
            password="pass1234",
        ),
        MemberMaster(
            member_name="石川　美香",
            address="名古屋市中区222-22",
            phone_number="07055667788",
            email="mika.ishikawa@example.com",
            password="pass1234",
        ),
    ]

    # データベースに追加
    db.session.bulk_save_objects(members)
    db.session.commit()

    # スタッフデータを作成
    staffs = [
        StaffMaster(
            account_name="staff_takahashi",
            staff_name="高橋　健次郎",
            division_name="経営本部",
            password="pass1234",
        ),
        StaffMaster(
            account_name="staff_saito",
            staff_name="斎藤　幸次",
            division_name="営業部",
            password="pass1234",
        ),
        StaffMaster(
            account_name="staff_fujimoto",
            staff_name="藤本　代紀",
            division_name="情報システム部",
            password="pass1234",
        ),
    ]

    # データベースに追加
    db.session.bulk_save_objects(staffs)
    db.session.commit()

    # 客室タイプデータを作成
    room_types = [
        RoomTypeMaster(
            roomtype_name="シングルルーム",
            roomtype_price=8000,
            roomtype_image_filename="single.webp",
            roomtype_description="シングルベッド1台のシンプルな客室",
            roomtype_facilities="WiFi, エアコン, テレビ",
            maximum_capacity=1,
        ),
        RoomTypeMaster(
            roomtype_name="ツインルーム",
            roomtype_price=12000,
            roomtype_image_filename="twin.webp",
            roomtype_description="シングルベッド2台の客室",
            roomtype_facilities="WiFi, エアコン, テレビ, 冷蔵庫",
            maximum_capacity=2,
        ),
        RoomTypeMaster(
            roomtype_name="スイートルーム",
            roomtype_price=25000,
            roomtype_image_filename="suite.webp",
            roomtype_description="キングサイズベッド1台とリビングスペース付きの高級客室",
            roomtype_facilities="WiFi, エアコン, テレビ, 冷蔵庫, バスルーム",
            maximum_capacity=4,
        ),
    ]

    # データベースに追加
    db.session.add_all(room_types)
    db.session.commit()

    # 客室データを作成（3部屋）
    rooms = [
        RoomMaster(room_no="101", roomtype_id=room_types[0].roomtype_id),
        RoomMaster(room_no="102", roomtype_id=room_types[1].roomtype_id),
        RoomMaster(room_no="103", roomtype_id=room_types[2].roomtype_id),
    ]

    db.session.add_all(rooms)
    db.session.commit()

    # 宿泊プランを作成（各部屋2つ）
    stay_plans = [
        # 101号室（シングルルーム）のプラン
        StayPlanMaster(
            stayplan_name="朝食付きプラン",
            stayplan_description="和洋選べる朝食付きのプラン",
            roomtype_id=room_types[0].roomtype_id,
            additional_charges=1000,
            stayplan_start_from=date(2025, 1, 1),
            stayplan_end_of=date(2025, 12, 31),
        ),
        StayPlanMaster(
            stayplan_name="素泊まりプラン",
            stayplan_description="お食事なしの宿泊プラン",
            roomtype_id=room_types[0].roomtype_id,
            additional_charges=0,
            stayplan_start_from=date(2025, 1, 1),
            stayplan_end_of=date(2025, 12, 31),
        ),
        # 102号室（ツインルーム）のプラン
        StayPlanMaster(
            stayplan_name="朝食＆夕食付きプラン",
            stayplan_description="豪華なディナー付きのプラン",
            roomtype_id=room_types[1].roomtype_id,
            additional_charges=3000,
            stayplan_start_from=date(2025, 1, 1),
            stayplan_end_of=date(2025, 12, 31),
        ),
        StayPlanMaster(
            stayplan_name="ファミリープラン",
            stayplan_description="家族向けの特別価格プラン",
            roomtype_id=room_types[1].roomtype_id,
            additional_charges=1500,
            stayplan_start_from=date(2025, 1, 1),
            stayplan_end_of=date(2025, 12, 31),
        ),
        # 103号室（スイートルーム）のプラン
        StayPlanMaster(
            stayplan_name="特別記念プラン",
            stayplan_description="記念日に最適な豪華プラン",
            roomtype_id=room_types[2].roomtype_id,
            additional_charges=5000,
            stayplan_start_from=date(2025, 1, 1),
            stayplan_end_of=date(2025, 12, 31),
        ),
        StayPlanMaster(
            stayplan_name="連泊割引プラン",
            stayplan_description="2泊以上でお得に宿泊できるプラン",
            roomtype_id=room_types[2].roomtype_id,
            additional_charges=-2000,  # 割引を表現
            stayplan_start_from=date(2025, 1, 1),
            stayplan_end_of=date(2025, 12, 31),
        ),
    ]

    # データベースに追加
    db.session.add_all(stay_plans)
    db.session.commit()

    print("Database initialized.")
