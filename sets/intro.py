""" 
Sets

A set is a collection which is unordered, unchangeable*, and unindexed.

This means that the items are unchangeable, but you can remove items and add new items.

Sets are written with the `set` keyword and double brackets or with curly brackets.
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
print(pets)

# Getting length
print(len(fruits))

# Getting type
print(type(fruits))

# Accessing items
print('banana' in fruits)