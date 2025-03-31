from unittest.mock import patch, MagicMock
from roomecho import app, db
from roomecho.models.StaffMaster import StaffMaster

@patch("roomecho.db.session.query")
def test_staff_view_del_01(mock_query, client):
    """No.01 テストケース名：スタッフ削除画面表示"""

    # モック設定
    mock_result = MagicMock()
    mock_result.get.return_value = []
    mock_query.return_value = mock_result

    # テスト実行
    with client.session_transaction() as session:
        session["loginId"] = "1"

    response = client.get("/staff/staff/1/del")
    print(response.data.decode("utf-8"))

    # 検証
    mock_query.assert_called_once_with(StaffMaster)
    mock_result.get.assert_called_once_with("1")

    assert response.status_code == 200


@patch('roomecho.db.session.commit')
@patch('roomecho.db.session.delete')
@patch('roomecho.db.session.query')
def test_staff_view_del_02(mock_query, mock_delete, mock_commit, client):
    """No.02 テストケース名：スタッフ削除完了画面表示"""

    ### Arrange（準備） ###
    # スタッフモック設定
    staff = StaffMaster()
    staff.user_id = 1

    # モック設定
    mock_result = MagicMock()
    mock_result.get.return_value = staff
    mock_query.return_value = mock_result

    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    response = client.post("/staff/staff/1/del")

    ### Assert（検証） ###
    # スタッフ情報取得が正しく行われたか確認
    mock_query.assert_any_call(StaffMaster)
    mock_result.get.assert_called_with("1")
    
    # スタッフ削除処理が正しく行われたか確認
    mock_delete.assert_called_once_with(staff)
    mock_commit.assert_called_once()
    
    # レスポンスの検証
    assert response.status_code == 200
