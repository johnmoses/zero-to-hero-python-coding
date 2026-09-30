"""
conftest.py

Fixtures defined here are automatically available to all test files
in this directory without any import.
"""
import pytest


@pytest.fixture
def sample_numbers():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def sample_user():
    return {"name": "Alice", "age": 30, "active": True}
