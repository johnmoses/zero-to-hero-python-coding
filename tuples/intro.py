""" 
Tuples
"""

# Empty tuple
t0 = ()
print(t0)

# Simple tuples
t1 = ('a', 'b', 'c', 'd', 'e')
print(t1)

t2 = tuple('abcde')
print(t2)

t3 = (1, 2, 3, 4, 5)
print(t3)

#Mixed types
t4 = ('1', '2', 'three', '1.5')
print(t4)

# Nested
t5 = ('James', ('Dev', 'Manager'))
print(t5)

# Get length of tupple
print(len(t5))

# Access items
print(t4[0])