from flask import render_template, request
from bmiex3 import app

# '/input' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/input', methods=['GET'])
def input():
    # BMI計算用の入力フォームを表示
    return render_template('bmi-input.html')

# '/bmi' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/bmi', methods=['POST'])
def bmi():
    # 入力エラーがあるかを判定するフラグ
    errflg = False

    # フォームのデータを取得
    height = request.form['height'] # ユーザーが入力した身長
    weight = request.form['weight'] # ユーザーが入力した体重
    height_err = '' # 身長のエラーメッセージ
    weight_err = '' # 体重のエラーメッセージ

    # バリデーション（入力チェック）
    # 身長が入力されていない場合
    if not height:
        errflg = True
        height_err = '身長を入力してください'
    # 身長が0以下の場合
    elif float(height) <= 0:
        errflg = True
        height_err = '身長は正の数を入力してください'

    # 体重が入力されていない場合
    if not weight:
        errflg = True
        weight_err = '体重を入力してください'
    # 体重が0以下の場合
    elif float(weight) <= 0:
        errflg = True
        weight_err = '体重は正の数を入力してください'

    # 入力エラーがある場合、再度入力フォームを表示
    if errflg:
        return render_template('bmi-input.html', height=height, weight=weight, height_err=height_err, weight_err=weight_err)

    # 入力された身長と体重を数値（float）に変換
    float_height = float(height)
    float_weight = float(weight)

    # BMIを計算（体重 ÷ 身長²）
    float_anser = float_weight / (float_height * float_height)

    # 小数点第2位までの値にフォーマット
    formatted_value = "{:.2f}".format(float_anser)

    # 計算結果を表示する
    return render_template('bmi-result.html', result=formatted_value)
