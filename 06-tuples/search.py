""" 
Search
"""

letters = ('a', 'b', 'c', 'd', 'e')
numbers = (1, 2, 3, 4, 5)

print('c' in letters)

# Using a function
def search_tuple(data, target):
    for i in data:
        if i == target:
            return data.index(i)
    return 'The element does not exist'

print(search_tuple(letters, 'c'))
print(search_tuple(numbers, '3'))