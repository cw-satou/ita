from flask import render_template, request
from itemsearch import app, db
from itemsearch.mst_item import mstItem

# '/items' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/items', methods=['GET'])
def items():
    # 商品テーブルを全件取得
    mst_items = db.session.query(mstItem).all()
    # 取得した商品データを一覧ページに渡して表示
    return render_template('item-list.html',items=mst_items)

# '/items/search' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/items/search', methods=['GET'])
def items_search():
    # クエリパラメータから検索条件（IDと名前）を取得
    id = request.args.get('id')  # 入力された商品IDを取得
    name = request.args.get('name')  # 入力された商品名を取得

    # 検索条件が空の場合は全件取得
    if not id and not name:
        # 全商品を取得
        mst_items = db.session.query(mstItem).all()
    # IDのみ指定された場合
    elif id and not name:
        # IDが一致する商品を取得
        mst_items = db.session.query(mstItem).filter(
            mstItem.id == id
        ).all()  # 結果をすべて取得
    # 名前のみ指定された場合
    elif not id and name:
        # 名前が部分一致する商品を取得
        mst_items = db.session.query(mstItem).filter(
            mstItem.name.like(f'%{name}%')
        ).all()  # 結果をすべて取得

    # 検索結果を一覧ページに渡して表示
    return render_template('item-list.html',items=mst_items)
