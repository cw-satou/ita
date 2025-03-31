from flask import render_template, request, redirect, url_for
from itemdelete import app, db
from itemdelete.mst_item import mstItem

# '/items' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/items', methods=['GET'])
def items():
    # 商品テーブルを全件取得
    mst_items = db.session.query(mstItem).all()
    # 商品情報を渡して表示
    return render_template('item-list.html', items=mst_items)

# '/items/<id>' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/items/<id>', methods=['GET'])
def items_confirm(id):
    # 商品IDを指定して1件取得
    mst_items = db.session.query(mstItem).get(id)
    # 商品情報を渡して表示
    return render_template('item-confirm.html', item=mst_items)

# '/items/delete' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/items/delete', methods=['POST'])
def items_delete():
    id = request.form['id']  # フォームから商品IDを取得

    # 指定されたIDの商品を取得
    mst_item = db.session.query(mstItem).get(id)
    if mst_item:  # 該当商品が存在する場合
        # データベースから該当商品を削除
        db.session.delete(mst_item)
        # 変更をデータベースに反映
        db.session.commit()

    # 商品一覧ページにリダイレクト
    return redirect(url_for('items'))
