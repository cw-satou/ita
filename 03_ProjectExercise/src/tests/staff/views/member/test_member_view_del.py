from unittest.mock import patch, MagicMock
from roomecho import app, db
from roomecho.models.MemberMaster import MemberMaster
from roomecho.models.Booking import Booking

@patch("roomecho.db.session.query")
def test_member_view_del_01(mock_query, client):
    """No.01 テストケース名：会員退会画面表示（最もシンプル版）"""

    # モック設定
    mock_result = MagicMock()
    mock_result.get.return_value = []
    mock_result.filter.return_value.count.return_value = 0
    mock_query.return_value = mock_result

    # テスト実行
    with client.session_transaction() as session:
        session["loginId"] = "1"

    response = client.get("/staff/member/1/del")

    # 検証
    mock_result.get.assert_called_once_with("1")

    assert response.status_code == 200


@patch('roomecho.db.session.commit')
@patch('roomecho.db.session.delete')
@patch('roomecho.db.session.query')
def test_member_view_del_02(mock_query, mock_delete, mock_commit, client):
    """No.02 テストケース名：会員退会完了画面表示"""

    ### Arrange（準備） ###
    # 会員モック設定
    member = MemberMaster()
    member.user_id = 1

    # モック設定
    mock_result = MagicMock()
    mock_result.get.return_value = member
    mock_result.filter.return_value.count.return_value = 0
    mock_query.return_value = mock_result

    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    response = client.post("/staff/member/1/del")

    ### Assert（検証） ###
    # 会員情報取得が正しく行われたか確認
    mock_query.assert_any_call(MemberMaster)
    mock_result.get.assert_called_with("1")
    
    # 予約情報確認が行われたか検証
    mock_query.assert_any_call(Booking)
    mock_result.filter.assert_called_once()
    
    # 会員削除処理が正しく行われたか確認
    mock_delete.assert_called_once_with(member)
    mock_commit.assert_called_once()
    
    # レスポンスの検証
    assert response.status_code == 200
