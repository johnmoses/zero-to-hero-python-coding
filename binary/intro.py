""" 
Demonstrate how to use binary types in Python."""
# Binary data type
# A byte is 8 bits
# A bit is either 0 or 1
# A byte can be interpreted in different ways, like binary, octal, or hexadecimal
# Binary is base 2
# Octal is base 8
# Hexadecimal is base 16
# In python, we can use the following functions to convert between different bases:
# bin() - converts to binary
# oct() - converts to octal
# hex() - converts to hexadecimal
# int() - converts to integer
# We can also use the following prefixes to represent different bases:
# 0b - binary
# 0o - octal
# 0x - hexadecimal
# Example:
# 10 in decimal is 1010 in binary, 12 in octal, and A in hexadecimal
# 0b1010 == 10
# 0o12 == 10
# 0xA == 10
# Let's see some examples:


# Convert to binary
print(bin(10))  # 0b1010
print(bin(255))  # 0b11111111
# Convert to octal
print(oct(10))  # 0o12
print(oct(255))  # 0o377
# Convert to hexadecimal
print(hex(10))  # 0xa
print(hex(255))  # 0xff
# Convert from binary to integer
print(int("0b1010", 2))  # 10
# Convert from octal to integer
print(int("0o12", 8))  # 10
# Convert from hexadecimal to integer
print(int("0xA", 16))  # 10
# Convert from string to integer
print(int("10"))  # 10
# Convert from integer to string
print(str(10))  # 10
# Convert from float to integer
print(int(10.5))  # 10
# Convert from integer to float
print(float(10))  # 10.0
# Convert from string
