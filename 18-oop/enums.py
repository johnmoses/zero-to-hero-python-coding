"""
Enums

Enums are named constants. They make code self-documenting and prevent
magic strings/numbers scattered across a codebase.
"""
from enum import Enum, auto


class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


order_status = OrderStatus.PENDING
print(order_status)          # OrderStatus.PENDING
print(order_status.value)    # pending
print(order_status.name)     # PENDING

# Compare by identity
if order_status == OrderStatus.PENDING:
    print("Order is waiting to be confirmed")

# Iterate all values
for status in OrderStatus:
    print(status.value)
