from itemregistauth import db

# 商品テーブルを表すモデルクラス
class Mst_items(db.Model):
    # テーブル名の指定
    __tablename__ = 'items'

    # 商品ID（主キー、オートインクリメント）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # 商品名（255文字まで、NULL禁止）
    name = db.Column(db.String(255), nullable=False)
    
    # 商品の価格（整数、NULL禁止）
    price = db.Column(db.Integer, nullable=False)
