# Testing

Testing verifies that your code behaves as expected. Python has built-in support via `unittest` and a popular third-party library `pytest`.

## unittest

`unittest` is Python's built-in testing framework, modelled after JUnit.

```py
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
```

## pytest

`pytest` is simpler and more expressive. Install with `pip install pytest`.

```py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2
```

Run with:

```sh
pytest
```

## Key concepts

- **Assertion** — checks that a condition is true
- **Test case** — a single unit of testing
- **Test suite** — a collection of test cases
- **Fixture** — setup/teardown logic shared across tests (`@pytest.fixture`)
- **Mocking** — replace real dependencies with controlled fakes (`unittest.mock`)
