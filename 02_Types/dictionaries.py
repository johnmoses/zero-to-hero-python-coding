'''
Dictionary
'''

# Updating an element
print('Updating')
dict = {'name': 'Edy', 'age': 26}
dict['address'] = 'London'
print(dict)

# Traversing
print('Traversing')
def traverseDict(d):
    for key in d:
        print(key, d[key])

traverseDict(dict)

# Searching
print('Searching')
def searchDict(d, value):
    for key in d:
        if d[key] == value:
            return key, value
    return 'The value does not exist'
print(searchDict(dict, 26))

print('Removing item')
# Removing an item
dict.pop('name')
print(dict)

# sort
print('Sorting')
dict = {'name': 'Peter', 'height': 4, 'complexion': 'fair', 'sex': 'male' }
print(dict)
print(sorted(dict, key=len))