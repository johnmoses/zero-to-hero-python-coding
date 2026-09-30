"""
Lambda Functions

A lambda is a small anonymous function defined in a single expression.
Syntax: lambda arguments: expression

Use lambdas for short, throwaway functions — especially as arguments
to higher-order functions like sorted(), map(), and filter().
"""

# Regular function vs lambda — equivalent
def add_ten(a):
    return a + 10

add_ten_lambda = lambda a: a + 10

print(add_ten(5))         # 15
print(add_ten_lambda(5))  # 15

# Multiple arguments
multiply = lambda a, b: a * b
print(multiply(5, 6))     # 30

# Three arguments
summarize = lambda a, b, c: a + b + c
print(summarize(5, 6, 2)) # 13

# Common use: key function in sorted()
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_by_age = sorted(people, key=lambda person: person[1])
print(sorted_by_age)      # sorted youngest to oldest

# Returning a lambda from a function (factory pattern)
def multiplier(n):
    return lambda a: a * n

doubler = multiplier(2)
tripler = multiplier(3)

print(doubler(11))   # 22
print(tripler(11))   # 33