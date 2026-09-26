""" 
Finally block
"""
try:
    print("Hello")
    print(1/0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This is finally block")
