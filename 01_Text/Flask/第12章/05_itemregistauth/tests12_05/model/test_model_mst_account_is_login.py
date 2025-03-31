import pytest
from flask import Flask, url_for
from itemregistauth.models.mst_accounts import is_login

# Flaskアプリのセットアップ
app = Flask(__name__)

# テスト用のクライアントを利用する
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config["SECRET_KEY"] = "testsecretkey"  # セッションを使用するために設定
    with app.test_client() as client:
        yield client

# ログイン情報がない時のリダイレクト先エンドポイントを登録
@app.route('/login')
def login():
    return "Please Login!"

# テストのためのエンドポイントを登録
@app.route('/protected')
@is_login
def protected_view():
    return "Welcome, Staff!"

def test_is_login_auth_succeeded(client):
    """ 正常系 セッションにログイン情報有り、先のページを表示 """

    ### Arrange（準備） ###
    # セッションにユーザーIDを格納
    with client.session_transaction() as sess:
        sess['loggedInUser'] = "管理者太郎"

    ### Act（実行） ### 
    response = client.get('/protected')
    
    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/protected"

def test_is_login_auth_failed(client):
    """ 準正常系 セッションにログイン情報無し、ログイン画面にリダイレクト """

    ### Arrange（準備） ###
    with client.session_transaction() as sess:
        sess.pop('loggedInUser', None)  # ログアウト状態を確保

    ### Act（実行） ### 
    response = client.get('/protected')
    
    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 302

    # リダイレクト先URLの確認
    assert response.headers['Location']=='/login'

    # エラーメッセージ（flashメッセージ）の確認
    with client.session_transaction() as sess:
        flash_messages = sess['_flashes'] if '_flashes' in sess else []    
    assert any("ログインしてください" in msg for _, msg in flash_messages)
