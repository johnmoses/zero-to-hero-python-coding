""" 
Local variable scope
"""
# Simple function

def simple():
    x = 300
    print(x)

simple()

# Nested function
def nested():
    x = 300
    def inner():
        print(x)
    inner()

nested()