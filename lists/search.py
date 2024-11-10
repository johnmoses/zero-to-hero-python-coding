""" 
Searching a list
"""

numbers = [1, 2, 3, 4, 5]

def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value was not found'
print(searchinList(numbers, 3))
