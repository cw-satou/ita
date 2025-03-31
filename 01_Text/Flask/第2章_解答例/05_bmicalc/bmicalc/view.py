from flask import request, render_template, redirect, url_for
from bmicalc import app

# '/input' にアクセスしたときの処理
@app.route('/input')
def input():
    # 入力フォームを表示
    return render_template('calc-input.html')

# '/bmi' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/bmi', methods=['POST'])
def calculate():
    # フォームから送信された身長と体重を取得し、浮動小数点数に変換
    height = float(request.form["height"])  # 身長を取得
    weight = float(request.form["weight"])  # 体重を取得
    
    # BMIを計算（体重 ÷ 身長²）
    result = weight / (height ** 2)

    # 計算結果をテンプレートに渡して表示
    return render_template('calc-result.html', result=result)
