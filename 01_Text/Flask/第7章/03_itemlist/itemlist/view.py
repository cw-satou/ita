from flask import render_template, request
from itemlist import app, db
from itemlist.mst_item import mstItem

# '/items' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/items', methods=['GET'])
def items():
    # 商品テーブルの全データを取得
    mst_items = db.session.query(mstItem).all()
    # 取得したデータを商品一覧ページに渡して表示
    return render_template('item-list.html', items=mst_items)

# '/items/<id>' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/items/<id>', methods=['GET'])
def items_id(id):
    # 指定したIDの商品を取得
    mst_items = db.session.query(mstItem).get(id)
    # 取得したデータを商品詳細ページに渡して表示
    return render_template('item-detail.html', item=mst_items)
