from flask import render_template, request
from calcvalidation import app

# '/input' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/input', methods=['GET'])
def input():
    # 入力フォームを表示
    return render_template('calc-input.html')

# '/calculate' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/calculate', methods=['POST'])
def calculate():
    # バリデーション（入力チェック）でエラーがあるかを判定するフラグ
    errflg = False

    # フォームのデータを取得し、初期値を設定
    num1 = request.form['num1'] # ユーザーが入力した数値1
    num2 = request.form['num2'] # ユーザーが入力した数値1
    num1err = ""
    num2err = ""

    # 数値1の入力チェック（空の場合はエラー）
    if not num1:
        errflg = True  # エラーフラグを立てる
        num1err = '数値1を入力してください' # エラーメッセージを設定

    # 数値2の入力チェック（空の場合はエラー）
    if not num2:
        errflg = True  # エラーフラグを立てる
        num2err = '数値2を入力してください' # エラーメッセージを設定

    # 入力エラーがあった場合、再び入力フォームを表示
    if errflg:
        return render_template('calc-input.html', num1=num1, num2=num2, num1err=num1err, num2err=num2err)

    # 入力された数値を整数に変換し、加算する
    int_num1 = int(num1)
    int_num2 = int(num2)
    # 2つの数値を加算
    sum = int_num1 + int_num2

    # 計算結果をテンプレートに渡して表示
    return render_template('calc-result.html', result=sum)
