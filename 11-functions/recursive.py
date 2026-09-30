"""
Recursive Functions

A recursive function calls itself to solve a smaller version of the same
problem. Every recursive function needs:
  1. A base case — the condition that stops the recursion
  2. A recursive case — the call that moves toward the base case
"""

# Classic example: factorial
# 5! = 5 x 4 x 3 x 2 x 1 = 120
def factorial(n):
    if n == 0:              # base case: 0! is defined as 1
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(5))   # 120
print(factorial(0))   # 1


# Countdown — simple visualisation of recursion unwinding
def countdown(n):
    if n <= 0:              # base case
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)   # recursive case: n shrinks each call

countdown(5)


# Fibonacci — each number is the sum of the two before it
# 0, 1, 1, 2, 3, 5, 8, 13 ...
def fibonacci(n):
    if n <= 1:              # base cases: fib(0)=0, fib(1)=1
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")   # 0 1 1 2 3 5 8 13