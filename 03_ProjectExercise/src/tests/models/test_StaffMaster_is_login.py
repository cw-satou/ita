import pytest
from flask import Flask, Blueprint, url_for
from roomecho.models.StaffMaster import StaffMaster

# Flaskアプリのセットアップ
app = Flask(__name__)
staff = Blueprint('staff', __name__, url_prefix="/staff")

# ログイン情報がない時のリダイレクト先エンドポイントを登録
@staff.route('/login')
def login():
    return "Please Login!"

# Blueprintをアプリケーションに登録
app.register_blueprint(staff)

# テスト用のクライアントを利用する
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config["SECRET_KEY"] = "testsecretkey"  # セッションを使用するために設定
    with app.test_client() as client:
        yield client

# テストのためのエンドポイントを登録
@app.route('/staff')
@StaffMaster.is_login
def protected_view():
    return "Welcome, Staff!"

def test_StaffMaster_02(client):
    """No.02 テストケース名：ログイン済み状態での画面表示"""

    ### Arrange（準備） ###
    # セッションにユーザーIDを格納
    with client.session_transaction() as sess:
        sess['loginId'] = "1"

    ### Act（実行） ### 
    response = client.get('/staff')
    
    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff"

def test_StaffMaster_03(client):
    """No.03 テストケース名：未ログイン状態でのリダイレクト処理"""

    ### Arrange（準備） ###
    # セッションをクリア（未ログイン状態を確保）
    with client.session_transaction() as sess:
        sess.clear()

    ### Act（実行） ### 
    response = client.get('/staff')
    
    ### Assert（検証） ### 
    assert response.status_code == 302
    assert response.headers['Location'] == '/staff/login'
    
    # フラッシュメッセージの確認
    with client.session_transaction() as sess:
        flash_messages = sess['_flashes'] if '_flashes' in sess else []    
    assert any("ログインしてください" in msg for _, msg in flash_messages)
