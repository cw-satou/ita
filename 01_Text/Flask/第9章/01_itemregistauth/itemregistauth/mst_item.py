from itemregistauth import db

# 商品テーブルを表すモデルクラス
class mstItem(db.Model):
    # テーブル名の指定（デフォルトではクラス名がテーブル名になるが、明示的に変更可能）
    __tablename__ = 'items'

    # 商品ID（主キー、オートインクリメント）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 商品名（最大255文字、NULL禁止）
    name = db.Column(db.String(255), nullable=False)

    # 商品の価格（整数型、NULL禁止）
    price = db.Column(db.Integer, nullable=False)
