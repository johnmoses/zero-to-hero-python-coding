"""
Models

Product dataclass and a simple in-memory store (dict).
In a real app this would be a database.
"""
from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class Product:
    id: int
    name: str
    price: float
    in_stock: bool = True


# In-memory store: {id: Product}
_store: Dict[int, Product] = {}
_next_id = 1


def all_products():
    return list(_store.values())

def get_product(product_id: int) -> Optional[Product]:
    return _store.get(product_id)

def create_product(name: str, price: float, in_stock: bool = True) -> Product:
    global _next_id
    product = Product(id=_next_id, name=name, price=price, in_stock=in_stock)
    _store[_next_id] = product
    _next_id += 1
    return product

def update_product(product_id: int, name: str, price: float, in_stock: bool) -> Optional[Product]:
    product = _store.get(product_id)
    if not product:
        return None
    product.name = name
    product.price = price
    product.in_stock = in_stock
    return product

def delete_product(product_id: int) -> bool:
    if product_id not in _store:
        return False
    del _store[product_id]
    return True
