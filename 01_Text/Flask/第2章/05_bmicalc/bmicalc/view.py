from flask import request, render_template
from bmicalc import app

# '/input' にアクセスしたときの処理
@app.route('/input')
def input():
    # 入力フォームを表示
    return render_template('calc-input.html')

# '/bmi' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/bmi', methods=['POST'])
def calculate():
    # 計算結果を表示
    return render_template('calc-result.html')
