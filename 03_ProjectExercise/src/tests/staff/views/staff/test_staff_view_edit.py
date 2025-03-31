from unittest.mock import patch, MagicMock
from flask import url_for
from roomecho import app, db
from roomecho.models.StaffMaster import StaffMaster

@patch('roomecho.db.session.query')
def test_staff_view_edit_01(mock_query, client):
    """No.01 テストケース名：スタッフ情報変更画面表示"""

    ### Arrange（準備） ###
    # モックの設定
    staff = StaffMaster()
    staff.staff_id = 1
    staff.account_name = "staff1"
    staff.staff_name = "スタッフ１"
    staff.division_name = "division1"
    staff.password = "pass1234"

    # モックの設定
    mock_result = MagicMock()
    mock_result.get.return_value = staff
    mock_query.return_value = mock_result
    
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"
    
    ### Act（実行） ###
    # GETリクエスト送信
    response = client.get("/staff/staff/1/edit")
    print(response.data.decode("utf-8"))

    ### Assert（検証） ###
    # スタッフ情報取得のクエリが呼ばれたか確認
    mock_result.get.assert_called_once_with("1")

    # レスポンスの検証
    assert response.status_code == 200
    assert response.request.path == "/staff/staff/1/edit"


def test_staff_view_edit_02(client):
    """No.02 テストケース名：スタッフ変更完了画面表示"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/staff/1/edit",
        data={
            "account_name": "staff1",
            "staff_name": "スタッフ１",
            "division_name": "division1"
        }
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/staff/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    assert "staff1" in returnHTML
    assert "スタッフ１" in returnHTML
    assert "division1" in returnHTML


def test_staff_view_edit_03(client):
    """No.03 テストケース名：スタッフ情報変更_アカウント名必須エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/staff/1/edit",
         data={
            "account_name": "",
            "staff_name": "スタッフ１",
            "division_name": "division1"
        }
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/staff/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[アカウント名]を入力してください" in returnHTML


def test_staff_view_edit_04(client):
    """No.04 テストケース名：スタッフ情報変更_アカウント名文字数超過エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/staff/1/edit",
        data={
            "account_name": "staff1234567890123",
            "staff_name": "スタッフ１",
            "division_name": "division1"
        }
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/staff/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[アカウント名]は15文字以内で入力してください" in returnHTML


def test_staff_view_edit_05(client):
    """No.05 テストケース名：スタッフ情報変更_スタッフ名必須エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/staff/1/edit",
        data={
            "account_name": "staff1",
            "staff_name": "",
            "division_name": "division1"
        }
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/staff/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[スタッフ名]を入力してください" in returnHTML


def test_staff_view_edit_06(client):
    """No.06 テストケース名：スタッフ情報変更_スタッフ名文字数超過エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/staff/1/edit",
        data={
            "account_name": "staff1",
            "staff_name": "スタッフ０１２３４５６７８０１２３４５６７８９０１２３４５６７８",
            "division_name": "division1"
        }
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/staff/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[スタッフ名]は30文字以内で入力してください" in returnHTML


def test_staff_view_edit_07(client):
    """No.07 テストケース名：スタッフ情報変更_所属名必須エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/staff/1/edit",
        data={
            "account_name": "staff1",
            "staff_name": "スタッフ１",
            "division_name": ""
        }
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/staff/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[所属名]を入力してください" in returnHTML


def test_staff_view_edit_08(client):
    """No.08 テストケース名：スタッフ情報変更_所属名文字数超過エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/staff/1/edit",
        data={
            "account_name": "staff1",
            "staff_name": "スタッフ１",
            "division_name": "division1212345678901234567890123"
        }
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/staff/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[所属名]は30文字以内で入力してください" in returnHTML

