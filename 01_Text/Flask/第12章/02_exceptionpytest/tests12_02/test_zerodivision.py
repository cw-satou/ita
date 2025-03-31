import pytest
from exceptionpytest import zerodivision

def test_div_numbers():
    with pytest.raises(ZeroDivisionError):
        zerodivision.div_numbers()
