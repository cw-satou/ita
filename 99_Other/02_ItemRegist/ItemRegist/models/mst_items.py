from ItemRegist.database import db

# 商品テーブルを表すモデルクラス
class Mst_items(db.Model):
    # テーブル名の指定（クラス名とは異なる名前を使いたい場合に明示的に指定）
    __tablename__ = 'items'

    # 商品ID（主キー、オートインクリメント）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # 商品名（255文字まで、NULL禁止）
    name = db.Column(db.String(255), nullable=False)
    
    # 商品の価格（整数、NULL禁止）
    price = db.Column(db.Integer, nullable=False)

    # コンストラクタ: 商品データを初期化
    def __init__(self, name, price):
        self.name = name  # 商品名を設定
        self.price = price  # 価格を設定
