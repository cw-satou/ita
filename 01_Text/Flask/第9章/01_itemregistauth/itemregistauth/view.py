from flask import render_template, flash, request, session, redirect, url_for
from itemregistauth import app, db
from .mst_account import mstAccount, is_login
from .mst_item import mstItem

# '/login' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/login', methods=['GET'])
def login():
    # ログイン画面を表示
    return render_template('login.html')

# '/login' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/login', methods=['POST'])
def login_exec():
    isLoginError = False  # エラーフラグを初期化
    user_id = request.form['user_id']  # フォームからユーザーIDを取得
    password = request.form['password']  # フォームからパスワードを取得

    # 入力エラーのチェック（ユーザーIDとパスワードが空でないか確認）
    if not user_id:
        isLoginError = True
        flash('ユーザIDは必須入力項目です。')  # ユーザーIDが未入力の場合にエラーメッセージを表示
    if not password:
        isLoginError = True
        flash('パスワードは必須入力項目です。')  # パスワードが未入力の場合にエラーメッセージを表示

    # データベース内の登録情報と一致するか確認
    mst_account = db.session.query(mstAccount).filter(
        mstAccount.user_id == user_id,  # ユーザーIDで検索
        mstAccount.password == password,  # パスワードで検索
    ).first()  # 一致する最初のレコードを取得

    # ログイン失敗時の処理
    if not mst_account:
        isLoginError = True
        flash('「user_id」と「password」が一致しません。')  # ユーザーIDとパスワードが一致しない場合にエラーメッセージを表示

    # エラーがある場合、ログイン画面を再表示
    if isLoginError:
        return render_template('login.html')

    # ログイン成功時の処理
    session['loggedInUser'] = mst_account.user_id  # セッションにユーザーIDを保存
    return render_template('item-input.html')  # 商品入力ページを表示

# '/logout' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/logout', methods=['GET'])
def logout():
    # セッションからログイン情報を削除
    session.pop('loggedInUser', None)
    # ログイン画面にリダイレクト
    return redirect(url_for('login'))

# '/input' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/input', methods=['GET'])
@is_login  # ログイン済みユーザーのみアクセスできるようにするデコレータ
def input():
    return render_template('item-input.html')  # 商品入力フォームを表示

# '/register' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/register', methods=['POST'])
@is_login  # ログイン済みユーザーのみアクセスできるようにするデコレータ
def register():
    # フォームから商品名と価格を受け取る
    name = request.form['name']
    price = request.form['price']

    # 商品情報をデータベースに登録
    mst_items = mstItem(name, price)  # 新しい商品インスタンスを作成
    db.session.add(mst_items)  # セッションに追加
    db.session.commit()  # トランザクションを確定してデータベースに保存

    # 登録後、すべての商品データを取得
    mst_items = db.session.query(mstItem).all()
    # 登録結果を表示するページに商品データを渡して表示
    return render_template('item-result.html', items=mst_items)
