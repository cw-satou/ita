from flask import request, render_template
from calcex1 import app

# '/input' にアクセスしたときの処理
@app.route('/input')
def input():
    # 入力フォームを表示
    return render_template('calc-input.html')

# '/calculate' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/calculate', methods=['POST'])
def calculate():
    # フォームから送信された3つの数値を取得し、それぞれ整数に変換
    number1 = int(request.form["num1"])  
    number2 = int(request.form["num2"])  
    number3 = int(request.form["num3"])  
    
    # 3つの数値を掛け算し、計算結果を変数resultに保存
    result = number1 * number2 * number3

    # 計算結果をテンプレートに渡して表示
    return render_template('calc-result.html', result=result)
