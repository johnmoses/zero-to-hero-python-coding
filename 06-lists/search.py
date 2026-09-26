""" 
Searching for an item in a list
"""

numbers = [1, 2, 3, 4, 5]
target = 4

def search(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value was not found'
print(search(numbers, target))
