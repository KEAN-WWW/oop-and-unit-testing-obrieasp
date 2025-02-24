import sys
import os

from app.addition import add

def test_addition():
    result = add(val1=2, val2=2)
    assert result == 4
