import pytest
from itemregistauth import app

@pytest.fixture
def client():
    """ Flaskのテストクライアント（コンテキスト付き） """
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "testsecretkey"
    with app.app_context():  # アプリケーションコンテキストを設定
        with app.test_client() as client:   # APPクライアントを設定
            yield client
