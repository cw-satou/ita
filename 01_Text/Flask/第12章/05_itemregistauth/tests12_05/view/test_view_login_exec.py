from unittest.mock import patch, MagicMock
from itemregistauth import app
from itemregistauth.models.mst_accounts import Mst_account

@patch("itemregistauth.db.session.query")  # query をモック
def test_login_success_redirect_input(mock_query, client):
    """ 正常系 ログイン成功、商品入力画面にリダイレクト """

    ### Arrange（準備） ###
    # モックの戻り値を設定
    mock_account = MagicMock(spec=Mst_account)
    mock_account.user_id = "testuser"
    mock_query.return_value.filter.return_value.first.return_value = mock_account

    ### Act（実行） ### 
    # # ビューの呼び出し
    # exec_function = None    # リクエストで呼び出されるビュー名（実行結果）
    # for rule in app.url_map.iter_rules():
    #     if rule.rule == "/login" and "POST" in rule.methods:
    #         exec_function = rule.endpoint

    # POSTリクエスト送信
    response = client.post("/login", data={"user_id": "testuser", "password": "testpass"})

    ### Assert（検証） ### 
    # # 呼び出した関数の確認
    # assert exec_function == "login_exec"

    # ステータスコードの確認
    assert response.status_code == 302

    # 表示URLの確認
    assert response.headers['Location']=='/input'

    # セッションにユーザーIDが格納されていることを確認
    with client.session_transaction() as sess:
        assert sess["loggedInUser"] == "testuser"

def test_login_failure_no_user_id(client):
    """ 準正常系 ユーザーID入力無し、ログイン画面にリダイレクト """

    ### Arrange（準備） ###

    ### Act（実行） ### 
    # POSTリクエスト送信
    response = client.post("/login", data={"user_id": "", "password": "testpass"})

    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 302

    # 表示URLの確認
    assert response.headers['Location']=='/login'

    # エラーメッセージ（flashメッセージ）の確認
    with client.session_transaction() as sess:
        flash_messages = sess['_flashes'] if '_flashes' in sess else []    
    assert any("ユーザIDは必須入力項目です。" in msg for _, msg in flash_messages)

def test_login_failure_no_password(client):
    """ 準正常系 パスワード入力無し、ログイン画面にリダイレクト """

    ### Arrange（準備） ###

    ### Act（実行） ### 
    # POSTリクエスト送信
    response = client.post("/login", data={"user_id": "testuser", "password": ""})

    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 302

    # 表示URLの確認
    assert response.headers['Location']=='/login'

    # エラーメッセージ（flashメッセージ）の確認
    with client.session_transaction() as sess:
        flash_messages = sess['_flashes'] if '_flashes' in sess else []    
    assert any("パスワードは必須入力項目です。" in msg for _, msg in flash_messages)

@patch("itemregistauth.db.session.query")  # `query` をモック
def test_login_failure_user_not_found(mock_query, client):
    """ 準正常系 ログイン失敗、ログイン画面にリダイレクト """

    ### Arrange（準備） ###

    # モックの戻り値を設定
    mock_query.return_value.filter.return_value.first.return_value = None

    ### Act（実行） ### 
    # POSTリクエスト送信
    response = client.post("/login", data={"user_id": "testuser", "password": "testpass"})

    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 302

    # 表示URLの確認
    assert response.headers['Location']=='/login'

    # エラーメッセージ（flashメッセージ）の確認
    with client.session_transaction() as sess:
        flash_messages = sess['_flashes'] if '_flashes' in sess else []    
    assert any("「user_id」と「password」が一致しません。" in msg for _, msg in flash_messages)
