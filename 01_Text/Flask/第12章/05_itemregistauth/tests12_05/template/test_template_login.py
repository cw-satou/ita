import webbrowser
import os
from flask import Flask, render_template, current_app

app = Flask(__name__, template_folder="..\\..\\itemregistauth\\templates")
app.config["TESTING"] = True

# ダミーのエンドポイントを登録
@app.route('/dummy', endpoint='login')
def dummy():
    return

# テスト関数
def test_template():

    ### Arrange（準備） ###

    ### Act（実行） ### 
    # テンプレートをレンダリング
    with app.test_request_context():

        rendered_html = render_template("login.html")
        assert rendered_html is not None, "テンプレートレンダリング処理エラー"

        # レンダリング結果をファイルに出力
        template = current_app.jinja_env.get_template("login.html")
        output_path = os.path.dirname(template.filename)
        output_file_path = os.path.join(output_path, '..', "test_"+"login.html")

        # `/static/`を`./static/`に置き換え
        rendered_html = rendered_html.replace('/static/', './static/')

        # 出力されたHTMLファイルを書き出し
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(rendered_html)

    ### Assert（検証） ### 
    # 出力したファイルをブラウザで開く
    webbrowser.open(output_file_path)
