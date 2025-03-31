import os
import sys

# ソースコードのあるディレクトリを設定（srcフォルダ）
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(src_path)

import pytest
from roomecho import app, db
from roomecho.models.MemberMaster import MemberMaster
from roomecho.models.StaffMaster import StaffMaster

# テスト用にFlaskクライアントを作成
@pytest.fixture
def client():
    """Flaskテストクライアント"""
    app.config['SERVER_NAME'] = 'localhost:5000'
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'secret_key'  # セッションを使うために設定
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def init_db():
    # 設定ファイルの読み込み
    app.config.from_pyfile("../config.py")

    # アプリケーションコンテキスト内でデータベース操作を実行
    with app.app_context():

        #テーブルの再作成
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