from roomecho import db

# 客室マスター
# 客室情報のマスターテーブル
# 客室を削除した場合はレコードを物理削除する

class RoomMaster(db.Model):
    __tablename__ = 'room_master'
    
    # 客室番号（"1001"、"0203"等の部屋番号）
    room_no = db.Column(db.CHAR(4), primary_key=True)
    
    # 客室タイプID
    roomtype_id = db.Column(db.Integer, nullable=False)
