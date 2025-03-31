from roomecho import db

# 予約データテーブル
class Booking(db.Model):
    __tablename__ = 'bookings'
    
    # 予約ID（自動採番）
    booking_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # 予約日時
    booking_datetime = db.Column(db.DateTime, nullable=False)
    
    # 会員ID
    member_id = db.Column(db.Integer, nullable=False)
    
    # 客室番号
    room_no = db.Column(db.CHAR(4), nullable=False)
    
    # プランID
    stayplan_id = db.Column(db.Integer, nullable=False)
    
    # 宿泊人数
    guest_count = db.Column(db.Integer, nullable=False)
    
    # 料金
    price = db.Column(db.Integer, nullable=False)
    
    # チェックイン日
    checkin_date = db.Column(db.Date, nullable=False)
    
    # チェックアウト日
    checkout_date = db.Column(db.Date, nullable=False)
