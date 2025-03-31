from itemregistauth import app

def test_input_auth_success(client):
    """ 正常系 セッションにログイン情報有り、商品入力ページを表示 """

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session['loggedInUser'] = 'テストユーザー'

    ### Act（実行） ### 
    # GETリクエスト送信
    response = client.get("/input")

    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == '/input'

def test_input_auth_failue(client):
    """ 準正常系 セッション情報無し、ログイン画面にリダイレクト """

    ### Arrange（準備） ###

    ### Act（実行） ### 
    # GETリクエスト送信
    response = client.get("/input")

    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 302

    # 表示URLの確認
    assert response.headers['Location']=='/login'
