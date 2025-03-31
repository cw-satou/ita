from flask import request, render_template, redirect
from calcredirect import app

# '/input' にアクセスしたときの処理
@app.route('/input')
def input():
    # 入力フォームを表示
    return render_template('calc-input.html')

# '/calculate' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/calculate', methods=['POST'])
def calculate():
    # フォームから2つの数値を取得し、整数に変換
    number1 = int(request.form["num1"])  
    number2 = int(request.form["num2"])  
    
    # 2つの数値を足し算し、計算結果を保存
    result = number1 + number2

    # 計算結果をURLパラメータとして '/calculate' にリダイレクト
    return redirect(f'/calculate?result={result}')

# '/calculate' にアクセスしたときの処理（リダイレクト後のページ）
@app.route('/calculate')
def calculate2():
    # URLパラメータから計算結果を取得し、整数に変換
    result = int(request.args.get('result'))

    # 計算結果をテンプレートに渡して表示
    return render_template('calc-result.html', result=result)
