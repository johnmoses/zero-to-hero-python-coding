""" 
Join
"""

fruits = {'banana', 'orange', 'mango', 'lemon'}
pets = set(("dogs", "cats", "parrots"))

# Union of two or more sets
everything = fruits.union(pets)
print(everything)

# Union of two or more sets with pipe
everything_1 = fruits | pets
print(everything_1)