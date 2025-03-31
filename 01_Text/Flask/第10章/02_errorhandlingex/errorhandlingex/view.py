from flask import render_template
from errorhandlingex import app
from werkzeug.exceptions import HTTPException

# '/err405' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/err405', methods=['POST'])
def err405():
    # POSTメソッド以外でアクセスすると「405 Method Not Allowed」エラーが発生する
    return render_template('err405.html')

# '/err500' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/err500', methods=['GET'])
def err500():
    # ここでゼロ除算（10 / 0）が発生し、500エラー（Internal Server Error）となる
    calc = 10 / 0  # 例外発生
    print('計算結果:', calc)  # この行は実行されない（前の行でエラー）

    # エラーが発生するとこのページは表示されず、500エラーとなる
    return render_template('err500.html')

# すべてのエラーをハンドリングし、カスタムエラーページを表示
@app.errorhandler(Exception)
def show_system_error_page(error):
        if isinstance(error, HTTPException):
            name = error.name
            code = error.code
            description = error.description
        else:
            # 発生したエラーから情報が取れない場合はステータスコード「500」の「Internal Server Error」とする
            name = "Internal Server Error"
            code = 500
            description = str(error)

        # カスタムエラーページ 'org_error.html' にエラー情報を渡して表示
        return render_template('org_error.html', name=name, code=code, description=description), code
