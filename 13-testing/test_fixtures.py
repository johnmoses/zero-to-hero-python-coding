"""
pytest Fixtures

Fixtures provide reusable setup logic shared across multiple tests.
Decorated with @pytest.fixture and injected as function parameters.
"""
import pytest


class Cart:
    def __init__(self):
        self.items = []

    def add(self, item, price):
        self.items.append({"item": item, "price": price})

    def total(self):
        return sum(i["price"] for i in self.items)

    def count(self):
        return len(self.items)


@pytest.fixture
def empty_cart():
    return Cart()

@pytest.fixture
def loaded_cart():
    cart = Cart()
    cart.add("apple", 1.50)
    cart.add("bread", 2.00)
    return cart


def test_empty_cart_total(empty_cart):
    assert empty_cart.total() == 0

def test_empty_cart_count(empty_cart):
    assert empty_cart.count() == 0

def test_add_item(empty_cart):
    empty_cart.add("milk", 1.20)
    assert empty_cart.count() == 1

def test_loaded_cart_total(loaded_cart):
    assert loaded_cart.total() == 3.50

def test_loaded_cart_count(loaded_cart):
    assert loaded_cart.count() == 2
