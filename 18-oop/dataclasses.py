"""
Dataclasses

@dataclass auto-generates __init__, __repr__, and __eq__ from field annotations.
Less boilerplate than writing them manually.
"""
from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True
    tags: list = field(default_factory=list)

    def discounted(self, pct: float) -> float:
        return self.price * (1 - pct / 100)


p = Product("Rice", 1500.0, tags=["food", "staple"])
print(p)
print(p.discounted(10))

# Equality is value-based (not identity-based)
p2 = Product("Rice", 1500.0, tags=["food", "staple"])
print(p == p2)  # True
