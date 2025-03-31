from flask import template_rendered
from calcdiv import app

def test_input():

    ### Arrange（準備） ###

    # Flask のテストクライアント（ビューのテストのために必要な部品）を作成
    client = app.test_client()

    ### Act（実行） ### 
    # GETリクエスト送信
    response = client.get("/")

    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 200
