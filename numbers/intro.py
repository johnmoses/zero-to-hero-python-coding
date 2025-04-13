"""
Numbers
Integers, Floats, Complex
"""
import random

x = 1  
print(type(x))

y = 2.8 
print(type(y))

z = 1j 
print(type(z))

# Integers
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Floating point numbers
print('Float')
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Complex numbers
print('Complex')
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Random numbers
print('Random')
x = random.random()
print(x)

y = random.choice([1,2,3,4])
print(y)

# Literals
print('Literals')
x = 0o1, 0o20, 0o377       # octal
print(x)

y = 0x01, 0x10, 0xff       # hex
print(y)

z = 0b1, 0b10000, 0b11111111   # binary
print(z)