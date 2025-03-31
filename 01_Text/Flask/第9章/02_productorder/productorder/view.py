from flask import render_template, request, flash, session, redirect, url_for
from productorder import app, db
from .mst_users2 import mstUsers2, is_login
import re  # 正規表現を扱うためのライブラリをインポート

# '/' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/', methods=['GET'])
def login():
    # ログイン画面に表示するメッセージを取得（デフォルトは「ログインしてください。」）
    message = request.args.get('message', 'ログインしてください。')
    return render_template('login.html', message=message)

# '/login' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/login', methods=['POST'])
def login_exec():
    isLoginError = False  # エラーフラグを初期化
    id = request.form['id']  # ユーザーIDを取得
    password = request.form['password']  # パスワードを取得

    # 入力エラーのチェック
    # ユーザーIDが未入力または6桁の英数字でない場合（チャレンジ問題）
    if not id or not re.fullmatch(r'[a-zA-Z0-9]{6}', id):
        isLoginError = True
        flash('ユーザーIDは6桁の英数字で入力してください。')

    # パスワードが未入力または5桁の数字でない場合（チャレンジ問題）
    if not password or not re.fullmatch(r'\d{5}', password):
        isLoginError = True
        flash('パスワードは5桁の数字で入力してください。')

    # データベースに登録されているか確認
    mst_account = db.session.query(mstUsers2).filter(
        mstUsers2.id == id,  # ユーザーIDで検索
        mstUsers2.password == password  # パスワードで検索
    ).first()  # 一致する最初のレコードを取得

    if not mst_account:
        isLoginError = True
        flash('ユーザーIDまたはパスワードが間違っています。')

    # エラーがある場合、ログイン画面を再表示
    if isLoginError:
        return redirect(url_for('login', message='エラーを確認してください。'))

    # ログイン成功時の処理
    session['loggedInUser'] = mst_account.id  # セッションにユーザーIDを保存
    return render_template('order.html', product='', quantity='')  # 注文入力画面を表示

# '/logout' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/logout', methods=['POST'])
def logout():
    #
    # ここにセッション情報を削除する処理を記載
    #
    return redirect(url_for('login', message='ログアウトしました。'))  # ログイン画面にリダイレクト

# '/order' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/order', methods=['GET'])
    #
    # ここにログインチェック処理を記載
    #
def order():
    isOrderError = False  # エラーフラグを初期化

    # クエリパラメータから商品名と数量を取得
    product = request.args.get('product')
    quantity = request.args.get('quantity')

    # 入力チェック
    if not product:
        flash('商品を選択してください。')
        isOrderError = True
    if not quantity:
        flash('数量を入力してください。')
        isOrderError = True
    elif not quantity.isdigit():  # 全桁が数字かチェック
        flash('数量は数字を入力してください。')
        isOrderError = True

    # エラーがある場合、注文入力画面を再表示
    if isOrderError:
        return render_template('order.html', product=product, quantity=quantity)

    # 注文が正しく入力された場合、結果画面を表示
    return render_template('result.html', product=product, quantity=quantity)

# '/back' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/back', methods=['POST'])
    #
    # ここにログインチェック処理を記載
    #
def back():
    # フォームから送信されたデータを取得
    product = request.form['product']  # 商品名
    quantity = request.form['quantity']  # 数量
    return render_template('order.html', product=product, quantity=quantity)  # 注文入力画面を再表示
