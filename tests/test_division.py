import pytest
import sys
import os

from app.divide import divide

def test_division():
    result = divide(val1=4, val2=2)
    assert result == 2

def test_divide_zero_exception():
    with pytest.raises(ZeroDivisionError):
        result = divide(val1=4, val2=0)
        assert result == 2