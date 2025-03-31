from flask import render_template, request, redirect, url_for
from itemupdate import app, db
from itemupdate.mst_item import mstItem

# '/items' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route("/items", methods=["GET"])
def items():
    # 商品テーブルを全件取得
    mst_items = db.session.query(mstItem).all()
    # 取得した商品データを一覧ページに渡して表示
    return render_template("item-list.html", items=mst_items)

# '/items/edit/<id>' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route("/items/edit/<id>", methods=["GET"])
def items_edit(id):
    # 商品IDを指定してデータを1件取得
    mst_items = db.session.query(mstItem).get(id)
    # 編集画面に取得した商品データを渡して表示
    return render_template("item-edit.html", item=mst_items)

# '/items/confirm' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route("/items/confirm", methods=["POST"])
def items_confirm():
    id = request.form['id']  # フォームからIDを取得
    name = request.form['name']  # フォームから商品名を取得
    price = request.form['price']  # フォームから単価を取得
    item = { 
        'id': id,
        'name': name,
        'price': price,
    }
    # 確認画面に取得したデータを渡して表示
    return render_template("item-confirm.html", item=item)

# '/items/update' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route("/items/update", methods=["POST"])
def items_update():
    id = request.form['id']  # フォームからIDを取得
    name = request.form['name']  # フォームから商品名を取得
    price = request.form['price']  # フォームから単価を取得

    # 指定されたIDで商品データを取得
    mst_item = mstItem.query.get(id)  # 主キーで検索
    if mst_item:  # 該当する商品データが存在する場合
        mst_item.name = name  # 商品名を更新
        mst_item.price = price  # 単価を更新
        db.session.commit()  # 変更をデータベースに保存

    # 商品一覧ページにリダイレクト
    return redirect(url_for('items'))
