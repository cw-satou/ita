from flask import render_template, request, session
from errorhandling import app

# '/err405' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/err405', methods=['POST'])
def err405():
    # クライアント（ブラウザ）からGETメソッドでアクセスされると
    # 対応する処理がないため「405 Method Not Allowed」エラーが発生する
    return render_template('err405.html')

# '/err500' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/err500', methods=['GET'])
def err500():
    # ここでゼロ除算（10 / 0）が発生
    # Pythonではゼロで割り算をすると例外（ZeroDivisionError）が発生する
    calc = 10 / 0  # 例外発生
    print('計算結果:', calc)  # この行は実行されない（前の行でエラー）

    # エラーが発生するとこのページは表示されず、500 Internal Server Error となる
    return render_template('err500.html')
