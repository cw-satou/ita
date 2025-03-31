from itemregistauth import app

def test_logout(client):

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session['loggedInUser'] = 'テストユーザー'

    ### Act（実行） ### 
    # GETリクエスト送信
    response = client.get("/logout")

    ### Assert（検証） ### 
    # セッションにユーザーIDが格納されていないことを確認
    with client.session_transaction() as sess:
        assert "loggedInUser" not in sess

    # ステータスコードの確認
    assert response.status_code == 302

    # 表示URLの確認
    assert response.headers['Location']=='/login'
