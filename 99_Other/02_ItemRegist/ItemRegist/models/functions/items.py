# データベース接続用のインスタンスとモデルをインポート
from ItemRegist.database import db
from ItemRegist.models.mst_items import Mst_items

# 商品データを登録する関数
# 引数:
# - name: 商品名 (文字列)
# - price: 商品の価格 (整数)
def registerItem(name, price):
    # 商品データのインスタンスを作成
    mst_items = Mst_items(name, price)
    
    # データベースセッションに商品を追加
    db.session.add(mst_items)
    
    # 変更をデータベースに確定
    db.session.commit()
    return

# すべての商品を取得する関数
# 戻り値: 商品のリスト
def getAllItems():
    # 商品テーブルをID順にソートして全件取得
    mst_items = Mst_items.query.order_by(Mst_items.id).all()
    return mst_items