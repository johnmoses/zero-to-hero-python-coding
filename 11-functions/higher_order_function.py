"""
Higher Order Functions

A higher-order function either:
  1. Takes a function as an argument, OR
  2. Returns a function as its result

Built-in examples: map(), filter(), sorted()
"""

# 1. Taking a function as an argument
def apply(func, value):
    """Calls func with value and returns the result."""
    return func(value)

def square(n):
    return n ** 2

def double(n):
    return n * 2

print(apply(square, 5))   # 25
print(apply(double, 5))   # 10

# 2. Built-in higher-order functions
numbers = [1, 2, 3, 4, 5]

# map() applies a function to every item
squared = list(map(square, numbers))
print(squared)            # [1, 4, 9, 16, 25]

# filter() keeps items where the function returns True
def is_even(n):
    return n % 2 == 0

evens = list(filter(is_even, numbers))
print(evens)              # [2, 4]

# sorted() accepts a key function
words = ["banana", "apple", "cherry"]
print(sorted(words, key=len))  # sorted by length

# 3. Returning a function
def multiplier(factor):
    """Returns a function that multiplies its input by factor."""
    def multiply(n):
        return n * factor
    return multiply

triple = multiplier(3)
print(triple(7))          # 21