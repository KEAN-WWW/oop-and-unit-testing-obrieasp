"""
Test cases for the addition functionality.
"""
from app.addition import add

def test_addition():
    """
    Test the addition of two numbers.
    """
    result = add(val1=2, val2=2)
    assert result == 4