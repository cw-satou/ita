import pytest
from calcdiv import app

@pytest.fixture
def client():
    return app.test_client()
