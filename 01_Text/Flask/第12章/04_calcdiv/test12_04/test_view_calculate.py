from flask import template_rendered
import pytest
from calcdiv import app

def test_calculate_case1(client):

    ### Arrange（準備） ###

    ### Act（実行） ### 
    # POSTリクエスト送信
    response = client.post("/calculate", data={"num1": "10", "num2": "2"})

    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 200

    # 計算結果の確認
    assert "5.0" in response.data.decode("utf-8")

def test_calculate_case2(client):

    ### Arrange（準備） ###

    ### Act（実行） ### 
    # POSTリクエスト送信
    response = client.post("/calculate", data={"num1": "0", "num2": "2"})

    # ステータスコードの確認
    assert response.status_code == 200

    # 計算結果の確認
    assert "0.0" in response.data.decode("utf-8")

def test_calculate_case3(client):

    ### Arrange（準備） ###

    ### Act（実行） ### 
    # POSTリクエスト送信
    with pytest.raises(ZeroDivisionError):
        response = client.post("/calculate", data={"num1": "5", "num2": "0"})
