from unittest.mock import patch, MagicMock
from roomecho import app, db
from roomecho.models.MemberMaster import MemberMaster

# 会員一覧画面表示のビューをテストする関数
@patch('roomecho.db.session.query')
def test_member_view_list_01(mock_query, client):
    """No.01 テストケース名：会員一覧画面表示"""

    # query.orderby().allの処理のモックを作成
    mock_order_by = MagicMock()
    mock_order_by.all.return_value = []
    mock_query.return_value.order_by.return_value = mock_order_by 

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # GETリクエスト送信
    response = client.get("/staff/member")

    ### Assert（検証） ###
    # モデル利用の処理が正しく行われているか確認
    mock_query.assert_called_once_with(MemberMaster)
    mock_query.return_value.order_by.assert_called_once_with("user_id")
    mock_order_by.all.assert_called_once()

    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/member"
