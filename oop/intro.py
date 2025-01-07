"""
OOP example
"""
# Creating or defining a class
class Apple:
    size = 3

# Creating object and instantiating a class
a = Apple()

# Accesing a property
print(a.size)

# Add more features
class Orange:
    # Constructor function or method
    def __init__(self, size, color):
        self.size = size
        self.color = color

    # String representation of the object
    def __str__(self):
        return f"{self.size}({self.color})"

    def describe(self):
        print(f"Orange is size {self.size} and color {self.color}")

o = Orange(3, "Green")
print(o)
print(o.size)
print(o.color)
o.describe()
