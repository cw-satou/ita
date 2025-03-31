from flask import render_template, request, flash, redirect, url_for
from itemregistauth import db
from itemregistauth.items import items_bp
from itemregistauth.items.models.mst_items import Mst_items
from itemregistauth.auth.models.mst_accounts import is_login

# "/input" にアクセスしたときの処理（商品入力画面の表示）
@items_bp.route("input", methods=["GET"])
@is_login  # ログインしているか確認
def input():
    return render_template("item-input.html")

# "/register" にアクセスしたときの処理（商品登録処理）
@items_bp.route("register", methods=["POST"])
@is_login  # ログインしているか確認
def register():
    # フォームから商品名と価格を取得
    name = request.form['name']
    price = request.form['price']

    # 入力チェック（どちらかが未入力の場合はエラー）
    isItemRegistError = False
    if not name:  # 商品名が入力されていない場合
        isItemRegistError = True

    if not price:  # 価格が入力されていない場合
        isItemRegistError = True

    # エラーがある場合は商品入力画面へリダイレクト
    if isItemRegistError:
        flash("商品名と単価はいずれも必須入力項目です。")
        return redirect(url_for('items.input'))

    # 新しい商品データを作成し、データベースに保存
    mst_items = Mst_items(name=name, price=price)
    db.session.add(mst_items)  # データベースに追加
    db.session.commit()  # データベースに変更を反映

    # 登録されている全商品を取得
    mst_items = Mst_items.query.order_by(Mst_items.id).all()

    # 商品データをリストに格納
    items = []
    for mst_item in mst_items:
        # 商品情報を辞書形式で保存
        item = { 
            'id': mst_item.id,
            'name': mst_item.name,
            'price': mst_item.price,
        }
        items.append(item)  # itemsリストに追加

    # 商品一覧画面を表示
    return render_template("item-result.html", items=items)
