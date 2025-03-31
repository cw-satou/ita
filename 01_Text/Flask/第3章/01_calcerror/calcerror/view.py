from flask import request, render_template
from calcerror import app

# '/input' にアクセスしたときの処理
@app.route('/input')
def input():
    # 入力フォームを表示
    return render_template('calc-input.html')

# '/calculate' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/calculate', methods=['POST'])
def calculate():
    # フォームから送信された2つの数値を取得し、整数に変換
    number1 = int(request.form["num1"])  
    number2 = int(request.form["num2"])  
    
    # 2つの数値を割り算し、計算結果を変数resultに保存
    result = number1 / number2

    # 計算結果をテンプレートに渡して表示
    return render_template('calc-result.html', result=result)
