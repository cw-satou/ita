from flask import render_template, flash, request, session, redirect, url_for
from itemregistauth import app, db
from .models.mst_items import Mst_items
from .models.mst_accounts import Mst_account, is_login

# "/login" にアクセスしたときの処理（ログイン画面を表示）
@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

# "/login" にアクセスしたときの処理（ログイン処理の実行）
@app.route("/login", methods=["POST"])
def login_exec():
    # ログインエラー判定用の変数
    isLoginError = False

    # フォームからユーザーIDとパスワードを取得
    user_id = request.form['user_id']
    password = request.form['password']

    # ユーザーIDの入力チェック
    if not user_id:
        isLoginError = True
        flash("{arg1}は必須入力項目です。".format(arg1='ユーザID'))

    # パスワードの入力チェック
    if not password:
        isLoginError = True
        flash("{arg1}は必須入力項目です。".format(arg1='パスワード'))

    # データベースから該当ユーザーを検索
    mst_account = db.session.query(Mst_account).filter(
        Mst_account.user_id == user_id,
        Mst_account.password == password,
    ).first()

    # 一致するアカウントがない場合、エラーメッセージを表示
    if not mst_account:
        isLoginError = True
        flash("「user_id」と「password」が一致しません。")

    # エラーがある場合はログイン画面へリダイレクト
    if isLoginError:
        return redirect(url_for('login'))

    # ログイン成功時、ユーザーIDをセッションに保存し、商品入力画面へリダイレクト
    session["loggedInUser"] = mst_account.user_id
    return redirect(url_for('input'))

# "/logout" にアクセスしたときの処理（ログアウト処理）
@app.route("/logout", methods=["GET"])
def logout():
    # セッションからログイン情報を削除
    session.pop('loggedInUser', None)
    return redirect(url_for('login'))

# "/input" にアクセスしたときの処理（商品入力画面の表示）
@app.route("/input", methods=["GET"])
@is_login  # ログイン認証が必要
def input():
    return render_template("item-input.html")

# "/register" にアクセスしたときの処理（商品登録処理）
@app.route("/register", methods=["POST"])
@is_login  # ログイン認証が必要
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
        return redirect(url_for('input'))

    # 新しい商品データを作成し、データベースに保存
    mst_items = Mst_items(name=name, price=price)
    db.session.add(mst_items)
    db.session.commit()

    # 登録された商品を取得
    mst_items = Mst_items.query.order_by(Mst_items.id).all()

    # 取得した商品データをリストに変換
    items = []
    for mst_item in mst_items:
        item = { 
            'id': mst_item.id,
            'name': mst_item.name,
            'price': mst_item.price,
        }
        items.append(item)

    # 登録結果画面を表示
    return render_template("item-result.html", items=items)
