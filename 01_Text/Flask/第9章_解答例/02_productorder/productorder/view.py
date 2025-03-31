from flask import render_template, request, flash, session, redirect, url_for
from productorder import app, db
from .mst_users2 import mstUsers2, is_login
import re  # 正規表現を使用するためのライブラリをインポート

# '/' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/', methods=['GET'])
def login():
    message = request.args.get('message')  # クエリパラメータからメッセージを取得
    if not message:
        message = 'ログインしてください。'  # デフォルトのメッセージ
    return render_template('login.html', message=message)

# '/login' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/login', methods=['POST'])
def login_exec():
    isLoginError = False  # エラーフラグを初期化

    # フォームから入力データを取得
    id = request.form['id']  # ユーザーID
    password = request.form['password']  # パスワード

    # 入力エラーのチェック
    if not id:
        isLoginError = True
        flash('ユーザIDは必須入力項目です。')  # ユーザーIDが未入力のエラーメッセージを表示
    if id and not re.match(r'^[a-zA-Z0-9]{6}$', id):  # 6桁の英数字であるかチェック
        isLoginError = True
        flash('6桁の英数字を入力してください。')

    if not password:
        isLoginError = True
        flash('パスワードは必須入力項目です。')  # パスワードが未入力のエラーメッセージを表示
    if password and not re.match(r'^[0-9]{5}$', password):  # 5桁の数字であるかチェック
        isLoginError = True
        flash('5桁の数字を入力してください。')

    # データベースからユーザー情報を検索
    mst_users2 = db.session.query(mstUsers2).filter(
        mstUsers2.id == id,  # ユーザーIDが一致
        mstUsers2.password == password  # パスワードが一致
    ).first()  # 最初に見つかったレコードを取得

    if not mst_users2:
        isLoginError = True
        flash('「user_id」と「password」が一致しません。')  # ユーザー情報が見つからなかった場合のエラー

    # エラーがあればログイン画面を再表示
    if isLoginError:
        return redirect(url_for('login', message="エラーを確認してください。"))

    # ログイン成功時の処理
    session['loggedInUser'] = mst_users2.id  # セッションにユーザーIDを保存
    return render_template('order.html', product='', quantity='')  # アイテム入力画面を表示

# '/logout' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('loggedInUser', None)  # セッション情報を削除
    return redirect(url_for('login', message='ログアウトしました。'))  # ログイン画面に遷移

# '/order' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/order', methods=['GET'])
@is_login  # ログイン済みのユーザーのみアクセス可能
def order():
    isOrderError = False  # エラーフラグを初期化

    # クエリパラメータから入力データを取得
    product = request.args.get('product')  # 商品名
    quantity = request.args.get('quantity')  # 数量

    # 入力エラーチェック
    if not product:
        flash('商品を選択してください。')  # 商品が未入力の場合のエラー
        isOrderError = True
    if not quantity:
        flash('数量を入力してください。')  # 数量が未入力の場合のエラー
        isOrderError = True
    if quantity and not quantity.isdigit():  # 数値であることを確認
        flash('数量は数字を入力してください。')
        isOrderError = True

    # エラーがある場合、注文画面を再表示
    if isOrderError:
        return render_template('order.html', product=product, quantity=quantity)

    # 正常に入力された場合、注文結果画面を表示
    return render_template('result.html', product=product, quantity=quantity)

# '/back' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/back', methods=['POST'])
@is_login  # ログイン済みのユーザーのみアクセス可能
def back():
    # フォームから送信されたデータを取得
    product = request.form['product']  # 商品名
    quantity = request.form['quantity']  # 数量

    return render_template('order.html', product=product, quantity=quantity)  # アイテム入力画面を表示
