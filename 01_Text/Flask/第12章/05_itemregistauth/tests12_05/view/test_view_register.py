from unittest.mock import patch, MagicMock
from itemregistauth import app

@patch("itemregistauth.view.Mst_items")     # Mst_items クラスをモック化
@patch("itemregistauth.db.session.add")     # add をモック化
@patch("itemregistauth.db.session.commit")  # commit をモック化
def test_register_auth_success_item_regist(mock_commit, mock_add, mock_Mst_items, client):
    """ 正常系、セッション情報あり、商品登録正常 """

    ### Arrange（準備） ###
    # 商品オブジェクトのモックを作成
    mock_item_instance = MagicMock()
    mock_item_instance.id = 1
    mock_item_instance.name = "テスト商品"
    mock_item_instance.price = 1000

    # query.order_by().all() のモックを作成
    mock_order_by = MagicMock()
    mock_order_by.all.return_value = [mock_item_instance]
    mock_query = MagicMock()
    mock_query.order_by.return_value = mock_order_by

    # query プロパティにモックを設定
    mock_Mst_items.query = mock_query

    # Mst_items(name, price) の呼び出しモックを設定
    mock_Mst_items.return_value = mock_item_instance

    # セッションデータを設定
    with client.session_transaction() as session:
        session['loggedInUser'] = 'テストユーザー'

    ### Act（実行） ### 
    # GETリクエスト送信
    response = client.post("/register", data={"name": "テスト商品", "price": 1000})

    ### Assert（検証） ### 
    # モデル利用の処理が正しく実行されていることを確認
    mock_Mst_items.assert_called_once()
    mock_add.assert_called_once_with(mock_item_instance)
    mock_commit.assert_called_once()
    mock_order_by.all.assert_called_once()

    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == '/register'

    # 画面にわたす情報の確認
    returnHTML = response.data.decode("utf-8")
    # print(returnHTML) 
    assert "テスト商品" in returnHTML
    assert "1000" in returnHTML

def test_register_no_item_name(client):
    """ 準正常系、セッション情報有り、商品名未入力 """

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session['loggedInUser'] = 'テストユーザー'

    ### Act（実行） ### 
    # GETリクエスト送信
    response = client.post("/register", data={"name": "", "price": "1000"})

    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 302

    # 表示URLの確認
    assert response.headers['Location']=='/input'


    # エラーメッセージ（flashメッセージ）の確認
    with client.session_transaction() as sess:
        flash_messages = sess['_flashes'] if '_flashes' in sess else []    
    assert any("商品名と単価はいずれも必須入力項目です。" in msg for _, msg in flash_messages)

def test_register_no_item_price(client):
    """ 準正常系、セッション情報有り、商品価格未入力 """

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session['loggedInUser'] = 'テストユーザー'

    ### Act（実行） ### 
    # GETリクエスト送信
    response = client.post("/register", data={"name": "テスト商品", "price": ""})

    ### Assert（検証） ### 
    # ステータスコードの確認
    assert response.status_code == 302

    # 表示URLの確認
    assert response.headers['Location']=='/input'


    # エラーメッセージ（flashメッセージ）の確認
    with client.session_transaction() as sess:
        flash_messages = sess['_flashes'] if '_flashes' in sess else []    
    assert any("商品名と単価はいずれも必須入力項目です。" in msg for _, msg in flash_messages)
