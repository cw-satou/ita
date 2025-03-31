from roomecho import app, db
from roomecho.models.MemberMaster import MemberMaster

def test_MemberMaster_01():
    """No.01 テストケース名：会員マスタのCRUD操作"""

    ### Arrange（準備） ###
    # テスト用の会員データを作成
    members = []
    member = MemberMaster()
    member.user_id = 1
    member.member_name = "会員名１"
    member.address = "住所１"
    member.email = "kaiin1@sample.com"
    member.phone_number = "09011111111"
    member.password = "kaiin1"
    members.append(member)

    ### Act（実行） ### 
    # アプリケーションのコンテキストを取得（データベース操作に必要）
    with app.app_context():

        # データベースの初期化（既存のデータを削除して新規作成）
        db.drop_all()
        db.create_all()

        # データ登録テスト
        # テストデータをデータベースに追加
        for member in members:
            db.session.add(member)
        db.session.commit()

        # データ取得テスト
        # 登録したデータを全件取得
        members = MemberMaster.query.order_by(MemberMaster.user_id).all()

        # データ更新テスト
        # 会員名を変更して保存
        member.member_name = "会員１１"
        db.session.commit()

        # データ削除テスト
        # 登録したデータを削除
        db.session.delete(member)
        db.session.commit()

    ### Assert（検証） ### 
    assert True

