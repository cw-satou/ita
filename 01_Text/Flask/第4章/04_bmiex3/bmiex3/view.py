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
    # バリデーション（入力チェック）でエラーがあるかを判定するフラグ
    errflg = False

    # フォームのデータを取得し、初期値を設定
    height = request.form['height'] # ユーザーが入力した身長
    weight = request.form['weight'] # ユーザーが入力した体重
    height_err = '' # 身長のエラーメッセージ
    weight_err = '' # 体重のエラーメッセージ

    # 身長が入力されていない、または0以下の時エラー
    # 体重が入力されていない、または0以下の時エラー

    # 入力エラーがあった場合、再び入力フォームを表示
    if errflg:
        return render_template('bmi-input.html', height=height, weight=weight, height_err=height_err, weight_err=weight_err)

    # 入力された身長と体重を浮動小数点数（float）に変換
    float_height = float(height)  # 身長を数値に変換
    float_weight = float(weight)  # 体重を数値に変換

    # BMIを計算（体重 ÷ 身長²）
    float_anser = float_weight / (float_height * float_height)

    # 小数点第2位までの値にフォーマット
    formatted_value = "{:.2f}".format(float_anser)

    # 計算結果を表示する
    return render_template('bmi-result.html', result=formatted_value)
