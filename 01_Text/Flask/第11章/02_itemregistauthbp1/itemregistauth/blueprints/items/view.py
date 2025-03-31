from flask import render_template, request, flash, redirect, url_for
from . import items_bp
from itemregistauth import db
from itemregistauth.models.mst_items import Mst_items
from itemregistauth.models.mst_accounts import is_login

# 商品入力画面を表示する処理を定義します
@items_bp.route("input", methods=["GET"])
@is_login  # このデコレーターでログインしているかを確認します
def input():
    # items/item-input.htmlというテンプレートをブラウザに表示します
    return render_template("items/item-input.html")

# 商品登録処理を行う関数です
@items_bp.route("register", methods=["POST"])
@is_login  # ログイン状態を確認します
def register():
    # フォームから送信された商品名と価格を取得します
    name = request.form['name']
    price = request.form['price']

    # 商品名が入力されていない場合、エラーを表示します
    if not name:
        isItemRegistError = True

    # 単価が入力されていない場合、エラーを表示します
    if not price:
        isItemRegistError = True

    # エラーがある場合はログイン画面に戻ります
    if 'isItemRegistError' in locals() and isItemRegistError:
        flash("商品名と単価はいずれも必須入力項目です。")
        return redirect(url_for('items.input'))

    # 新しい商品データを作成し、データベースに保存する準備をします
    mst_items = Mst_items(name=name, price=price)
    db.session.add(mst_items)  # データベースに追加
    db.session.commit()  # データベースに変更を反映

    # 全ての商品データを取得してリスト形式で整形します
    mst_items = Mst_items.query.order_by(Mst_items.id).all()
    items = []
    for mst_item in mst_items:
        # 商品データを辞書形式に変換してリストに追加します
        item = { 
            'id': mst_item.id,
            'name': mst_item.name,
            'price': mst_item.price,
        }
        items.append(item)

    # items/item-result.htmlというテンプレートに商品リストを渡して表示します
    return render_template("items/item-result.html", items=items)
