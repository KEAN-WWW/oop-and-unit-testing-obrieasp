"""
Test cases for the subtraction functionality.
"""

import pytest

from app.subtraction import subtract

def test_subtraction():
    """
    Test the subtraction of two numbers.
    """
    result = subtract(val1=4, val2=2)
    assert result == 2
