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
print(first, second, third)

# Getting variables from users
value1 = int(input('Enter a number: '))
value2 = int(input('Enter another number: '))
sum = value1 + value2
print(value1, " + ", value2, " = ", sum)