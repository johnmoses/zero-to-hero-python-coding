"""
Testing with pytest

Simpler than unittest — plain functions, plain assert statements.
Run with: pytest test_pytest.py
"""


def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0


def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(5, 0) == 0

def test_multiply_negative():
    assert multiply(-2, 3) == -6

def test_is_even_true():
    assert is_even(4) is True

def test_is_even_false():
    assert is_even(7) is False
