from unittest.mock import patch, MagicMock
from flask import url_for
from roomecho import app, db
from roomecho.models.MemberMaster import MemberMaster

@patch('roomecho.db.session.query')
def test_member_view_edit_01(mock_query, client):
    """No.01 テストケース名：会員情報変更画面表示"""

    ### Arrange（準備） ###
    # モックの設定
    member = MemberMaster()
    member.user_id = 1
    member.member_name = "会員一郎"
    member.email = "kaiin1@sample.com"
    member.address = "住所１"
    member.phone_number = "09011111111"

    # モックの設定
    mock_result = MagicMock()
    mock_result.get.return_value = member
    mock_query.return_value = mock_result
    
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"
    
    ### Act（実行） ###
    # GETリクエスト送信
    response = client.get("/staff/member/1/edit")
    print(response.data.decode("utf-8"))

    ### Assert（検証） ###
    # 会員情報取得のクエリが呼ばれたか確認
    mock_result.get.assert_called_once_with("1")

    # レスポンスの検証
    assert response.status_code == 200
    assert response.request.path == "/staff/member/1/edit"


def test_member_view_edit_02(client):
    """No.02 テストケース名：会員変更完了画面表示"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/member/1/edit",
        data={
            "member_name": "会員名１",
            "email": "kaiin1@sample.com",
            "address": "住所１",
            "phone_number": "09011111111",
        },
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/member/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    assert "会員名１" in returnHTML
    assert "kaiin1@sample.com" in returnHTML
    assert "住所１" in returnHTML
    assert "09011111111" in returnHTML


def test_member_view_edit_03(client):
    """No.03 テストケース名：会員情報変更_会員名必須エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/member/1/edit",
        data={
            "member_name": "",
            "email": "kaiin1@sample.com",
            "address": "住所１",
            "phone_number": "09011111111",
        },
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/member/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[会員名]を入力してください" in returnHTML


def test_member_view_edit_04(client):
    """No.04 テストケース名：会員情報変更_会員名文字数超過エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/member/1/edit",
        data={
            "member_name": "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほま",
            "email": "kaiin1@sample.com",
            "address": "住所１",
            "phone_number": "09011111111",
        },
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/member/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[会員名]は30文字以内で入力してください" in returnHTML


def test_member_view_edit_05(client):
    """No.05 テストケース名：会員情報変更_メールアドレス必須エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/member/1/edit",
        data={
            "member_name": "会員１",
            "email": "",
            "address": "住所１",
            "phone_number": "09011111111",
        },
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/member/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[メールアドレス]を入力してください" in returnHTML


def test_member_view_edit_06(client):
    """No.06 テストケース名：会員情報変更_メールアドレス文字数超過エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/member/1/edit",
        data={
            "member_name": "会員１",
            "email": "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890@sample.com",
            "address": "住所１",
            "phone_number": "09011111111",
        },
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/member/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[メールアドレス]は254文字以内で入力してください" in returnHTML


def test_member_view_edit_07(client):
    """No.07 テストケース名：会員情報変更_メールアドレス形式エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/member/1/edit",
        data={
            "member_name": "会員１",
            "email": "kaiin1sample.com",
            "address": "住所１",
            "phone_number": "09011111111",
        },
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/member/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[メールアドレス]はメールアドレスの形式で入力してください" in returnHTML


def test_member_view_edit_08(client):
    """No.08 テストケース名：会員情報変更_電話番号必須エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/member/1/edit",
        data={
            "member_name": "会員１",
            "email": "kaiin1@sample.com",
            "address": "住所１",
            "phone_number": "",
        },
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/member/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[電話番号]を入力してください" in returnHTML


def test_member_view_edit_09(client):
    """No.09 テストケース名：会員情報変更_電話番号文字数不足エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/member/1/edit",
        data={
            "member_name": "会員１",
            "email": "kaiin1@sample.com",
            "address": "住所１",
            "phone_number": "123456789",
        },
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/member/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[電話番号]は10文字～11文字以内で入力してください" in returnHTML


def test_member_view_edit_10(client):
    """No.10 テストケース名：会員情報変更_電話番号文字数超過エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/member/1/edit",
        data={
            "member_name": "会員１",
            "email": "kaiin1@sample.com",
            "address": "住所１",
            "phone_number": "123456789012",
        },
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/member/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[電話番号]は10文字～11文字以内で入力してください" in returnHTML


def test_member_view_edit_11(client):
    """No.11 テストケース名：会員情報変更_住所必須エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/member/1/edit",
        data={
            "member_name": "会員１",
            "email": "kaiin1@sample.com",
            "address": "",
            "phone_number": "09011111111",
        },
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/member/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[住所]を入力してください" in returnHTML


def test_member_view_edit_12(client):
    """No.12 テストケース名：会員情報変更_住所文字数不足エラー"""

    ### Arrange（準備） ###
    # セッションデータを設定
    with client.session_transaction() as session:
        session["loginId"] = "1"

    ### Act（実行） ###
    # POSTリクエスト送信
    response = client.post(
        "/staff/member/1/edit",
        data={
            "member_name": "会員１",
            "email": "kaiin1@sample.com",
            "address": "あいうえおかきくけこさしすせそたちつてとなにぬねのあいうえおかきくけこさしすせそたちつてとなにぬねのあいうえおかきくけこさしすせそたちつてとなにぬねのあいうえおかきくけこさしすせそたちつてとなにぬねのあいうえおかきくけこさしすせそたちつてとなにぬねのあいうえおかきくけこさしすせそたちつてとなにぬねのあいうえおかきくけこさしすせそたちつてとなにぬねのあいうえおかきくけこさしすせそたちつてとなにぬねのあいうえおかきくけこさしすせそたちつてとなにぬねのあいうえおかきくけこさしすせそたちつてとなにぬねのあいうえお",
            "phone_number": "123456789",
        },
    )

    ### Assert（検証） ###
    # ステータスコードの確認
    assert response.status_code == 200

    # 表示URLの確認
    assert response.request.path == "/staff/member/1/edit"

    # 画面に渡す情報の確認
    returnHTML = response.data.decode("utf-8")
    print(returnHTML)
    assert "[電話番号]は10文字～11文字以内で入力してください" in returnHTML
