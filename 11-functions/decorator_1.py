"""
Decorator 1 — Manual application

A decorator is a function that wraps another function to extend its
behaviour without modifying it. This file shows the manual (explicit)
way before introducing the @ syntax in decorator_2.py.

Pattern:
    decorated = decorator(original_function)
"""

def greet():
    return 'Hello'

def uppercase_decorator(function):
    """Wraps function so its return value is uppercased."""
    def wrapper():
        result = function()       # call the original function
        return result.upper()     # extend: uppercase the result
    return wrapper                # return the wrapper, not the result

# Manual application — explicitly passing the function
decorated_greet = uppercase_decorator(greet)
print(decorated_greet())   # HELLO

# The original is unchanged
print(greet())             # Hello