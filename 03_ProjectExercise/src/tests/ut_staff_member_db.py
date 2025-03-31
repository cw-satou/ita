import os
import sys
from sqlalchemy import create_engine,text

src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(src_path)

from roomecho import app, db
from roomecho.models.StaffMaster import StaffMaster
from roomecho.models.MemberMaster import MemberMaster

# データベースの作成
app.config.from_pyfile("../config.py")
engine = create_engine(
    url = app.config.get("SQLALCHEMY_DATABASE_BASE_URI"),
    isolation_level="AUTOCOMMIT"
)
engine.connect().execute(text("DROP DATABASE roomecho"))
engine.connect().execute(text("CREATE DATABASE roomecho"))

db.drop_all()
db.create_all()

# 会員データを作成
member = MemberMaster()
member.member_name="会員名１"
member.address="住所１"
member.phone_number="09011111111"
member.email="kaiin1@sample.com"
member.password="kaiin1"
db.session.add(member)
db.session.commit()

# スタッフデータを作成
staff = StaffMaster()
staff.account_name="staff1",
staff.staff_name="スタッフ１",
staff.division_name="所属１",
staff.password="staff1",
db.session.add(staff)
db.session.commit()

print("Database initialized.")
