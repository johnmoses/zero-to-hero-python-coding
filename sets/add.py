""" 
Add items
"""

fruits = {'banana', 'orange', 'mango', 'lemon'}
pets = set(("dogs", "cats", "parrots"))

fruits.add('pawpaw')
print('Added:', fruits)

# Add two sets together
fruits.update(pets)
print(fruits)

# Add any iterable
animals = ["antelope", "monkey"]
fruits.update(animals)
print(fruits)