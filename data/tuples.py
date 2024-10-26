'''
Tuples
'''

# Empty tuple
T0 = ()

# Simple
T1 = ('a', 'b', 'c', 'd', 'e')
T2 = tuple('abcde')
T3 = (1, 2, 3, 4, 5)

#Mixed types
T4 = ('1', '2', 'three', '1.5')

# Nested
T5 = ('James', ('Dev', 'Manager'))

# Displaying tuples
print('Displaying')
print(T0)
print(T1)
print(T2)
print(T3)
print(T4)
print(T5)

# Indexing
print('Indexing')
print(T1[0])

# Nested array
print(T5[0][0])

# Sequence operations
print('Sequences')
print(len(T1))

# Iterating
print('Iterating')
for i in T1:
    print(i)

# Concatenating
print('Concatenating')
print(T2 + T3)
print(T2 * 2)

# Membership
print('Membership')
Tm = [x ** 2 for x in T3]
print(Tm)

# Similarly
for index in range(len(T3)):
    print(T3[index])

# Searching
print('Searching')
print('c' in T1)
