from flask import render_template, request
from itemregist import app, db
from itemregist.mst_item import mstItem

# '/input' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/input', methods=['GET'])
def input():
    # 商品登録用の入力フォーム表示
    return render_template('item-input.html')

# '/register' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/register', methods=['POST'])
def register():
    # フォームから送信されたデータを取得
    name = request.form['name']
    price = request.form['price']

    # 商品データをデータベースに登録
    mst_items = mstItem(name=name, price=price)  # 商品モデルのインスタンスを作成
    db.session.add(mst_items)  # データベースのセッションに追加
    db.session.commit()  # 変更をデータベースに反映

    # 登録されたすべての商品データを取得
    mst_items = db.session.query(mstItem).all()

    # 登録結果を表示する
    return render_template('item-result.html', items=mst_items)
