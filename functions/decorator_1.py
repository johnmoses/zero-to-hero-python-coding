""" 
Decorator 1
"""

def greet():
    return 'Hello'

def decorate(function):
    def wrapper():
        func = function()
        to_uppercase = func.upper()
        return to_uppercase
    return wrapper

print(decorate(greet))