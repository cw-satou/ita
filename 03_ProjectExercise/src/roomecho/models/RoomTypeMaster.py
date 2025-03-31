from roomecho import db

# 客室タイプマスタテーブル
class RoomTypeMaster(db.Model):
    __tablename__ = "roomtype_master"

    # 客室タイプID（自動採番）
    roomtype_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 客室タイプ名
    roomtype_name = db.Column(db.String(50), nullable=False)

    # 宿泊料金
    roomtype_price = db.Column(db.Integer, nullable=False)

    # 客室画像
    roomtype_image_filename = db.Column(db.String(254), nullable=False)

    # 客室説明
    roomtype_description = db.Column(db.Text, nullable=False)

    # 設備備品
    roomtype_facilities = db.Column(db.Text, nullable=False)

    # 宿泊可能人数
    maximum_capacity = db.Column(db.Integer, nullable=False)
