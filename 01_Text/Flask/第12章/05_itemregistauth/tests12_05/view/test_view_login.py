from itemregistauth import app

def test_login(client):
    """ 正常系 ログインページを表示 """

    ### Arrange（準備） ###

    ### Act（実行） ### 
    # GETリクエスト送信
    response = client.get("/login")

    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == '/login'
