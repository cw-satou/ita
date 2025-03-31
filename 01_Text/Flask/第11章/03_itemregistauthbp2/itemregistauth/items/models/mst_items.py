from itemregistauth import db

# 商品情報を管理するテーブルのモデルクラス
class Mst_items(db.Model):
    # 使用するデータベーステーブル名を指定
    __tablename__ = 'items'

    # 商品ID（主キー、自動インクリメント）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # 商品名（255文字まで、NULL禁止）
    name = db.Column(db.String(255), nullable=False)
    
    # 商品の価格（整数型、NULL禁止）
    price = db.Column(db.Integer, nullable=False)
