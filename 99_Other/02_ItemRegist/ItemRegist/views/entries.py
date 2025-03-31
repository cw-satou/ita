# FlaskフレームワークとHTMLテンプレートを表示するための関数をインポート
from flask import render_template, request
from ItemRegist.__init__ import app
from ItemRegist.models.functions.items import registerItem, getAllItems

# -----------------------------------------------------------

# 入力フォームを表示するルート
@app.route("/input", methods=["GET"])
def input():
    # Item-input.html をブラウザに表示
    return render_template("/Item-input.html")

# 商品データを登録するルート
@app.route("/register", methods=["POST"])
def register():
    # フォームから送信されたデータを取得
    name = request.form['name']  # 商品名
    price = request.form['price']  # 価格

    # 商品データをデータベースに登録
    registerItem(name, price)

    # 登録済みのすべての商品データを取得
    mst_items = getAllItems()
    
    # データベースのデータをテンプレートで使いやすい形に変換
    items = []
    for mst_item in mst_items:
        item = {
            'id': mst_item.id,       # 商品ID
            'name': mst_item.name,   # 商品名
            'price': mst_item.price, # 価格
        }
        items.append(item)

    # 登録結果を表示するテンプレートをレンダリング
    return render_template("/Item-result.html", items=items)
