import sys
import os

from app.subtraction import subtract

def test_subtraction():
    result = subtract(val1=4, val2=2)
    assert result == 2