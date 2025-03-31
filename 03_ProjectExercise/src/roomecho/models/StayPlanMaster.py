from roomecho import db

# 宿泊プランマスター
class StayPlanMaster(db.Model):
    __tablename__ = 'stayplan_master'
    
    # 宿泊プランID（自動採番）
    stayplan_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # 宿泊プラン名（例："素泊まり"、"朝食付き"等）
    stayplan_name = db.Column(db.String(100), nullable=False)
    
    # 宿泊プラン説明（例："大満足バイキング形式の朝食付き"）
    stayplan_description = db.Column(db.Text, nullable=False)
    
    # 客室タイプID
    roomtype_id = db.Column(db.Integer, nullable=False)
    
    # 追加料金
    additional_charges = db.Column(db.Integer, nullable=False)
    
    # 宿泊プラン開始日
    stayplan_start_from = db.Column(db.Date)
    
    # 宿泊プラン終了日
    stayplan_end_of = db.Column(db.Date)
