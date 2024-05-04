"""
More numbers
"""

# Random numbers
print('Random numbers')
import random
r = random.random()
print(r)

c = random.choice([1,2,3,4])
print(c)

# Complex numbers
print('Complex numbers')
cx = 2 + 3j
print(cx)

cx = 1j * 1j
print(cx)

# Literals
print('Literals')
lx = 0o1, 0o20, 0o377       # octal
print(lx)

lx = 0x01, 0x10, 0xff       # hex
print(lx)

lx = 0b1, 0b10000, 0b11111111   # binary
print(lx)

# Other tools
print('Other tools')
import math

print(math.pi)
print(math.e)
print(math.sin(2 * math.pi / 180))
print(math.sqrt(144))
print(math.floor(3.1235))               # next lower integer
print(math.trunc(-2.4321))              # drop decimal digits
print(pow(2,4), 2 ** 4, 2.0 ** 4.0)
print(abs(-42))
print(min(1,3,5,7))
print(max(1,2,3,4))
print(round(5.234), round(5.643))