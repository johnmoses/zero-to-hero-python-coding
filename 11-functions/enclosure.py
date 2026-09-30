"""
Closures (Enclosures)

A closure is an inner function that remembers variables from its enclosing
scope even after the outer function has finished executing.

Three conditions for a closure:
  1. There is a nested (inner) function
  2. The inner function refers to a variable in the outer function
  3. The outer function returns the inner function
"""

# Basic closure — inner function captures 'first' from outer scope
def make_adder(first):
    def add(num):
        return num + first   # 'first' is remembered from outer scope
    return add               # return the function, not the result

add_10 = make_adder(10)      # 'first' is now locked in as 10
add_20 = make_adder(20)

print(add_10(5))   # 15
print(add_20(5))   # 25

# Real-world use: factory functions
def make_greeting(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

hello = make_greeting("Hello")
hi = make_greeting("Hi")

print(hello("Alice"))   # Hello, Alice!
print(hi("Bob"))        # Hi, Bob!