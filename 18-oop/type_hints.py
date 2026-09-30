"""
Type Hints

Type hints document expected types and catch bugs early with tools like mypy.
They are NOT enforced at runtime — Python still runs untyped code.

Run type check with: mypy type_hints.py
"""
from typing import Optional, Union, List, Dict


def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # returns str or None

def process(value: Union[int, float]) -> float:
    return float(value) * 1.1

def total(prices: List[float]) -> float:
    return sum(prices)

def describe(person: Dict[str, Union[str, int]]) -> str:
    return f"{person['name']} is {person['age']} years old"


print(greet("Alice"))
print(add(2, 3))
print(find_user(1))
print(find_user(99))   # None
print(process(10))
print(total([1.5, 2.0, 3.5]))
print(describe({"name": "Bob", "age": 25}))
