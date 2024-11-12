""" 
Sets
"""

# Creating an empty set
st = set()
print(st)

# Creating with initial elemennts
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)

mixed = {"apple", "banana", "cherry", True, 1, 2} # True and 1 are same
print(mixed)

# Creating with sets constructor
# This uses double brackets
pets = set(("dogs", "cats", "parrots"))

# Getting length
print(len(fruits))

# Getting type
print(type(fruits))

# Accessing items
print('banana' in fruits)