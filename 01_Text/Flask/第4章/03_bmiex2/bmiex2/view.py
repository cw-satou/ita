from flask import render_template, request
from bmiex2 import app

# '/input' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/input', methods=['GET'])
def input():
    # 入力フォームを表示するHTMLテンプレートをレンダリング
    return render_template('bmi-input.html')

# '/bmi' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/bmi', methods=['POST'])
def bmi():
    # フォームから送信されたデータを取得
    str_height = request.form['height']
    str_weight = request.form['weight']

    # 文字列の入力値を数値（float型）に変換
    float_height = float(str_height)
    float_weight = float(str_weight)

    # BMIを計算（体重 ÷ 身長²）
    float_anser = float_weight / (float_height * float_height)

    # 小数点第2位までの値にフォーマット
    formatted_value = "{:.2f}".format(float_anser)

    # 計算結果を表示する
    return render_template('bmi-result.html', result=formatted_value)
