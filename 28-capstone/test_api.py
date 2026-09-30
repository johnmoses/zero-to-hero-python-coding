"""
Capstone Tests

Full test suite for the Products API using pytest + httpx TestClient.
Run with: pytest test_api.py -v
"""
import pytest
from fastapi.testclient import TestClient

import models
from main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_store():
    """Reset in-memory store before each test."""
    models._store.clear()
    models._next_id = 1


def test_list_empty():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == []

def test_create_product():
    response = client.post("/products", json={"name": "Rice", "price": 1500.0})
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Rice"
    assert data["price"] == 1500.0
    assert data["in_stock"] is True

def test_get_product():
    client.post("/products", json={"name": "Bread", "price": 500.0})
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Bread"

def test_get_product_not_found():
    response = client.get("/products/99")
    assert response.status_code == 404

def test_update_product():
    client.post("/products", json={"name": "Milk", "price": 800.0})
    response = client.put("/products/1", json={"name": "Milk", "price": 900.0, "in_stock": False})
    assert response.status_code == 200
    assert response.json()["price"] == 900.0
    assert response.json()["in_stock"] is False

def test_update_product_not_found():
    response = client.put("/products/99", json={"name": "X", "price": 1.0, "in_stock": True})
    assert response.status_code == 404

def test_delete_product():
    client.post("/products", json={"name": "Egg", "price": 200.0})
    response = client.delete("/products/1")
    assert response.status_code == 204
    assert client.get("/products/1").status_code == 404

def test_delete_product_not_found():
    response = client.delete("/products/99")
    assert response.status_code == 404

def test_list_multiple():
    client.post("/products", json={"name": "A", "price": 100.0})
    client.post("/products", json={"name": "B", "price": 200.0})
    response = client.get("/products")
    assert len(response.json()) == 2
