"""
Test cases for the multiplication functionality.
"""

import pytest

from app.multiply import multiply

def test_multiplication():
    """
    Test the multiplication of two numbers.
    """
    result = multiply(val1=2, val2=2)
    assert result == 4
