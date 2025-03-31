# Flaskから必要な機能をインポートしています。
# - request: ユーザーがフォームで入力したデータを受け取るためのものです。
# - render_template: HTMLテンプレートを使ってページを表示するためのものです。
# - redirect: 別のURLに移動させる（リダイレクトする）ためのものです。
# - url_for: 他の関数に対応するURLを動的に生成します。
from flask import request, render_template, redirect, url_for

# calcモジュールからFlaskアプリケーション(app)をインポートします。
# appはWebアプリ全体を管理する基本のオブジェクトです。
from calc import app

# '/'または'/input'にアクセスしたときに実行される処理を定義します。
@app.route('/')
@app.route('/input')
def input():
    # calc-input.htmlというテンプレートを表示します。
    # このHTMLには、2つの数値を入力するフォームがあります。
    return render_template('calc-input.html')

# '/calculate'にPOSTメソッドでアクセスしたときに実行される処理を定義します。
@app.route('/calculate', methods=['POST'])
def calculate():
    # フォームから送信された2つの数値を取得し、それぞれ整数に変換します。
    number1 = int(request.form["num1"])  # 1つ目の数値を取得します。
    number2 = int(request.form["num2"])  # 2つ目の数値を取得します。
    
    # 2つの数値を足し算し、計算結果を変数resultに保存します。
    result = number1 + number2

    # 計算結果をURLパラメータとして渡し、/calculate2にリダイレクトします。
    return redirect(url_for('calculate2', result=result))

# '/calculate'にGETメソッドでアクセスしたときに実行される処理を定義します。
@app.route('/calculate')
def calculate2():
    # URLパラメータから計算結果を取得し、整数に変換します。
    result = int(request.args.get('result'))

    # calc-result.htmlというテンプレートを表示します。
    # このテンプレート内で計算結果が画面に表示されます。
    return render_template('calc-result.html', result=result)
