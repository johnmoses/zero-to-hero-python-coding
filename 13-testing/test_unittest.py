"""
Testing with unittest

Python's built-in testing framework. Test classes inherit from unittest.TestCase.
"""
import unittest


def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_mixed(self):
        self.assertEqual(add(-1, 1), 0)


class TestDivide(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(divide(10, 2), 5)

    def test_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_float_result(self):
        self.assertAlmostEqual(divide(1, 3), 0.333, places=3)


if __name__ == "__main__":
    unittest.main()
