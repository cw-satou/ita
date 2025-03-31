from itemlist import db

# 商品情報を管理するモデルクラス（データベースのテーブルと対応）
class mstItem(db.Model):
    # テーブル名を明示的に指定（デフォルトではクラス名がそのままテーブル名になる）
    __tablename__ = 'items'

    # 商品ID（主キー、オートインクリメント）
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 商品名（最大255文字、NULL禁止）
    name = db.Column(db.String(255), nullable=False)

    # 商品の価格（整数型、NULL禁止）
    price = db.Column(db.Integer, nullable=False)
