""" 
Math in Python
"""

import math

# Value of PI (3.14...)
print(math.pi)

# Exponent
print(math.e)

# Sine
print(math.sin(2 * math.pi / 180))

# Square root of a number
print(math.sqrt(144))

# Drop decimal digits
print(math.trunc(-2.4321))

# Value of x to the power of y
print(pow(2,4), 2 ** 4, 2.0 ** 4.0)

# Absolute (positive) value of the specified number
print(abs(-42))

# Lowest or highest value in an iterable
print(min(1, 3, 5, 7))
print(max(1, 2, 3, 4))

# Rounding numbers
print(round(5.234), round(5.643))
print(math.ceil(1.4))    # upwards to its nearest integer
print(math.floor(1.4))   # downwards to its nearest integer