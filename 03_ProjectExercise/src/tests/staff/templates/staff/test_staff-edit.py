import webbrowser
import os
from roomecho.models.StaffMaster import StaffMaster
from flask import Flask, Blueprint, render_template, current_app, session

# プロジェクトのルートディレクトリを取得
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

# テンプレートフォルダのパスを環境に依存しない方法で指定
template_dir = os.path.join(project_root, 'roomecho', 'staff', 'templates')

# テンプレートのテスト用アプリケーションを作成
app = Flask(__name__, template_folder=template_dir)
app.config["TESTING"] = True
app.config["SECRET_KEY"] = "test_secret_key"  # セッション用

# テスト用のダミー画面をルートに設定（実際の画面表示には影響しない）
@app.route("/", endpoint="staff.member_list")
@app.route("/staffs", endpoint="staff.staff_list")
@app.route("/staff/menu", endpoint="staff.menu")
@app.route("/staff/logout", endpoint="staff.logout")
@app.route("/staff/add", endpoint="staff.staff_add")
def dummy():
    return

@app.route("/staff/<staff_id>/edit", endpoint="staff.staff_edit")
@app.route("/staff/<staff_id>/del", endpoint="staff.staff_del")
def dummy(staff_id):
    return


# スタッフ編集画面テンプレートをテストする関数
def test_staff_edit_01(client):
    """No.01 テストケース名：テンプレート「スタッフ情報変更画面」表示"""

    ### Arrange（準備） ###
    # テスト対象の編集画面テンプレートを指定
    template_file = "staff/staff-edit.html"

    # テスト用スタッフデータを作成（編集対象のスタッフ情報）
    staff = StaffMaster()
    staff.staff_id = 1
    staff.account_name = "staff1"
    staff.staff_name = "スタッフ１"
    staff.division_name = "division1"
    staff.password = "pass1234"

    # 各入力項目のエラーメッセージを設定（テスト用仮想エラー）
    err_account_name = "アカウント名入力エラー"
    err_staff_name = "スタッフ名入力エラー"
    err_division_name = "所属名入力エラー"
    err_password = "パスワード入力エラー"


    ### Act（実行） ### 
    # テスト用のリクエスト環境を構築
    with app.test_request_context():
 
        # テンプレートに会員データを渡してHTMLを生成
        rendered_html = render_template(
            template_file,
            staff=staff,
            err_staff_name=err_staff_name,
            err_account_name=err_account_name,
            err_division_name=err_division_name,
            err_password=err_password
        )
        assert rendered_html is not None, "NG: テンプレートレンダリング処理エラー"

        # レンダリング結果をファイルに出力
        template = current_app.jinja_env.get_template(template_file)
        output_path = os.path.dirname(template.filename)
        output_file_name = "test_" + os.path.basename(template_file)
        output_file_path = os.path.join(output_path, output_file_name)
 
        # CSSや画像の参照パスをテスト用に変更
        rendered_html = rendered_html.replace("/static", "../../../static")

        # 生成したHTMLをファイルに書き込み
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(rendered_html)

    ### Assert（検証） ### 
    # 生成されたHTMLファイルをブラウザで自動表示
    webbrowser.open(output_file_path)
