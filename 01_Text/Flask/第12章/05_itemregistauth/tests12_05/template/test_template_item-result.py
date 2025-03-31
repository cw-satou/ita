import webbrowser
import os
from flask import Flask, render_template, current_app, session
from itemregistauth.models.mst_items import Mst_items

app = Flask(__name__, template_folder="..\\..\\itemregistauth\\templates")
app.config["TESTING"] = True
app.config["SECRET_KEY"] = "test_secret_key"  # セッション用

# ダミーのエンドポイントを登録
@app.route('/dummy', endpoint='input')
@app.route('/dummy', endpoint='logout')
def dummy():
    return

# テスト関数
def test_template():

    ### Arrange（準備） ###
    # テスト対象のテンプレートを定義
    template_file = "item-result.html"

    # テスト用のデータを作成
    items = [
        Mst_items(id = 1, name = "テスト商品１", price = 1100),
        Mst_items(id = 2, name = "テスト商品２", price = 1200),
        Mst_items(id = 3, name = "テスト商品３", price = 1300),
    ]

    ### Act（実行） ### 
    # テンプレートをレンダリング
    with app.test_request_context():

        # セッションデータを設定
        session['loggedInUser'] = "管理者一郎"

        rendered_html = render_template(template_file, items = items)

        assert rendered_html is not None, "テンプレートレンダリング処理エラー"

        # レンダリング結果をファイルに出力
        template = current_app.jinja_env.get_template(template_file)
        output_path = os.path.dirname(template.filename)
        output_file_path = os.path.join(output_path, '..', "test_"+template_file)

        # `/static/`を`./static/`に置き換え
        rendered_html = rendered_html.replace('/static/', './static/')

        # 出力されたHTMLファイルを書き出し
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(rendered_html)

    ### Assert（検証） ### 
    # 出力したファイルをブラウザで開く
    webbrowser.open(output_file_path)
