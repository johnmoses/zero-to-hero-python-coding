"""
Mocking with unittest.mock

Mocking replaces real dependencies (APIs, databases, files) with controlled fakes
so tests are fast, isolated, and repeatable.
"""
from unittest.mock import patch, MagicMock


def fetch_price(product_id):
    """Calls an external API — we mock this in tests."""
    import requests
    response = requests.get(f"https://api.example.com/prices/{product_id}")
    return response.json()["price"]

def get_discount(product_id):
    price = fetch_price(product_id)
    return price * 0.9


# --- Tests ---

@patch("requests.get")
def test_fetch_price(mock_get):
    mock_get.return_value.json.return_value = {"price": 100}
    assert fetch_price("abc") == 100
    mock_get.assert_called_once_with("https://api.example.com/prices/abc")

@patch("__main__.fetch_price", return_value=200)
def test_get_discount(mock_fetch):
    result = get_discount("xyz")
    assert result == 180.0
    mock_fetch.assert_called_once_with("xyz")

def test_magic_mock():
    db = MagicMock()
    db.find.return_value = [{"name": "Alice"}]
    result = db.find({"active": True})
    assert result[0]["name"] == "Alice"
    db.find.assert_called_once_with({"active": True})
