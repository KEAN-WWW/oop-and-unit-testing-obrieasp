import sys
import os


oop_project_path = "/Users/aspen/PycharmProjects/OOP"
sys.path.append(oop_project_path)

from app.addition import add

def test_addition():
    result = add(val1=2, val2=2)
    assert result == 4
