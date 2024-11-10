""" 
Bitwise Operators
"""

a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101
print('1 => a = ',a,':',bin(a),'b = ',b,':',bin(b))

c = 0

c = a & b;  # a AND b
print('2 => ',c,':',bin(c))

c = a | b;  # a OR b
print('3 => ',c,':',bin(c))

c = a ^ b;  # EXOR
print('4 => ',c,':',bin(c))

c = ~a  # complement
print('5 => ',c,':',bin(c))

c = a << 2  # left shift
print('6 => ',c,':',bin(c))

c = a >> 2 # right shift
print('7 => ',c,':',bin(c))