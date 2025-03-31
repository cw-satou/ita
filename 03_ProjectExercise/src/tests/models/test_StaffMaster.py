from roomecho import app, db
from roomecho.models.StaffMaster import StaffMaster

def test_StaffMaster_01():
    """No.01 テストケース名：スタッフマスタのCRUD操作"""
    
    # アプリケーションのコンテキストを取得（データベース操作に必要）
    with app.app_context():
        # テスト用のスタッフデータを作成
        staffs = []
        staff = StaffMaster()
        staff.staff_id = 1
        staff.account_name = "staff1"
        staff.staff_name = "スタッフ１"
        staff.division_name = "division1"
        staff.password = "staff1"
        staffs.append(staff)

        # データベースの初期化（既存のデータを削除して新規作成）
        db.drop_all()
        db.create_all()

        # データ登録テスト
        # テストデータをデータベースに追加
        for staff in staffs:
            db.session.add(staff)
        db.session.commit()

        # データ取得テスト
        # 登録したデータを全件取得
        staffs = StaffMaster.query.order_by(StaffMaster.staff_id).all()

        # データ更新テスト
        # スタッフ名を変更して保存
        staff.staff_name = "スタッフ１１"
        db.session.commit()

        # データ削除テスト
        # 登録したデータを削除
        db.session.delete(staff)
        db.session.commit()
