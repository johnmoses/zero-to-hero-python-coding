""" 
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Syntax:
    lambda arguments : expression
"""

# Addition
def x(a):
      return a + 10
print("Add:", x(5))

# Multiplication
x = lambda a, b: a * b
print("Multiply: ", x(5, 6))

# Summarize
# x = lambda a, b, c : a + b + c
# print("Summarize: ", x(5, 6, 2))

def summarize(a,b,c):
      return lambda a, b, c: a + b + c

print('Summarize: ',summarize(5, 6, 2))

# Do many things
def myfunc(n):
      return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print("Doubler: ", mydoubler(11))
print("Trippler: ", mytripler(11))