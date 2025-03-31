import webbrowser
import os
from roomecho.models.MemberMaster import MemberMaster
from flask import Flask, Blueprint, render_template, current_app, session

# プロジェクトのルートディレクトリを取得
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

# テンプレートフォルダのパスを環境に依存しない方法で指定
template_dir = os.path.join(project_root, 'roomecho', 'staff', 'templates')

app = Flask(__name__, template_folder=template_dir)
app.config["TESTING"] = True
app.config["SECRET_KEY"] = "test_secret_key"  # セッション用

# テスト用のダミー画面をルートに設定（実際の画面表示には影響しない）
@app.route("/", endpoint="staff.member_list")
@app.route("/staffs", endpoint="staff.staff_list")
@app.route("/staff/menu", endpoint="staff.menu")
@app.route("/staff/logout", endpoint="staff.logout")
def dummy():
    return

@app.route("/staff/<user_id>/edit", endpoint="staff.member_edit")
@app.route("/staff/<user_id>/del", endpoint="staff.member_del")
def dummy(user_id):
    return

# スタッフ用会員退会画面のテンプレートをテストする関数
def test_staff_member_edit_01(client):
    """No.01 テストケース名：テンプレート「会員退会画面」表示"""

    ### Arrange（準備） ###
    # テスト対象のテンプレートを定義
    template_file = "member/staff-member-del.html"

    # テスト用の会員データを作成
    member = MemberMaster()
    member.user_id = 1
    member.member_name = "会員名１"
    member.address = "住所１"
    member.email = "kaiin1@sample.com"
    member.phone_number = "09011111111"

    # 削除エラー時のメッセージを設定
    err_message = "エラーメッセージ"

    ### Act（実行） ### 
    # テスト用のリクエスト環境を構築
    with app.test_request_context():

        # セッションデータを設定
        session["loginId"] = "1"
    
        # テンプレートに会員データとエラーメッセージを渡してHTML生成
        rendered_html = render_template(
            template_file,
            member=member,
            err_message=err_message
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
