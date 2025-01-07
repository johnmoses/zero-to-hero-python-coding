"""
Data, values and types
"""
a = 1
b = 2
c = -45.17
d = 100
e = 10

# Displaying values stored in variables
print(a)
print(b)
print(c)
print(d)
print(e)

# Dynamic typing or change of values at runtime
a = 10
print('First, variable a has value', a, 'and type', type(a))
a = 'ABC'
print('Now, variable a has value', a, 'and type', type(a))

# Declaring multiple variables in one line
first, second, third = 'First', 'Second', 'Third'
print('First, second, third: ', first, second, third)

# Getting data type
x = 5
print('Type: ', type(x))

# Setting data type
x = "Hello World"
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))

# Getting variables from users
value1 = int(input('Enter a number: '))
value2 = int(input('Enter another number: '))
sum = value1 + value2
print(value1, " + ", value2, " = ", sum)
