"""
Decorator 2 — @ syntax and practical patterns

The @ symbol is syntactic sugar for: func = decorator(func)
It is the standard way to apply decorators in real code.
"""
import time

# Basic decorator with @ syntax
def uppercase_decorator(function):
    def wrapper():
        return function().upper()
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print(greeting())   # WELCOME TO PYTHON


# Practical pattern 1: timing decorator
def timer(function):
    """Measures and prints how long a function takes to run."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        print(f"{function.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

print(slow_sum(1_000_000))


# Practical pattern 2: stacking decorators
def bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def italic(function):
    def wrapper():
        return f"<i>{function()}</i>"
    return wrapper

@bold
@italic
def say_hello():
    return "Hello"

print(say_hello())   # <b><i>Hello</i></b>