"""
Test cases for the division functionality.
"""
import pytest
from app.divide import divide

def test_division():
    """
    Test the division of two numbers.
    """
    result = divide(val1=4, val2=2)
    assert result == 2

def test_divide_zero_exception():
    """
    Test division by zero raises ZeroDivisionError.
    """
    with pytest.raises(ZeroDivisionError):
        divide(val1=4, val2=0)
