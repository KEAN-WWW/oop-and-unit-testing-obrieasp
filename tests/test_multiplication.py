import sys
import os


oop_project_path = "/Users/aspen/PycharmProjects/OOP"
sys.path.append(oop_project_path)

from app.multiply import multiply

def test_multiplication():
    result = multiply(val1=2, val2=2)
    assert result == 4