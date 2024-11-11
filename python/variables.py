""" 
Variables
"""

a = 10
print('First, variable a has value', a, 'and type', type(a))
a = 'ABC'
print('Now, variable a has value', a, 'and type', type(a))

x = 5
y = "Hello, World!"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Cast
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# Get type
x = 5
y = "Hello, World!"
print(type(x))
print(type(y))

# See case-sensitivity
a = 4
A = "Sally"
print(a)
print(A)

# Camel case
myVariableName = "Joy"

# Pascal case
MyVariableName = "Joy"

# Snake case
my_variable_name = "Joy"

# Multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global
x = "fantastic!"

def glofunc():
  print("This is " + x)

glofunc()
print("This is " + x)

# Global with keyword
y = "great!"

def glofunc_1():
  global y
  y = "awesome!"
  print("This is " + y)

glofunc_1()
print("This is " + y)