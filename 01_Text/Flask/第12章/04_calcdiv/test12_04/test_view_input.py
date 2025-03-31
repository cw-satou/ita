from calcdiv import app

def test_input(client):

    ### Arrange（準備） ###

    ### Act（実行） ### 
    # GETリクエスト送信
    response = client.get("/")

    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 200
