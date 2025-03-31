from flask import request, render_template
from calc import app

# '/input'にアクセスしたときの処理
@app.route('/input')
def input():

    # 入力フォームを表示
    return render_template('calc-input.html')

# '/calculate'にアクセスしたときの処理
@app.route('/calculate', methods=['POST'])
def calculate():

    # フォームから2つの数値を取得
    number1 = int(request.form["num1"]) 
    number2 = int(request.form["num2"]) 
    
    # 2つの数値を足し算し、計算結果を変数resultに保存
    result = number1 + number2

    # 処理結果をテンプレートに渡して表示
    return render_template('calc-result.html', result=result)
