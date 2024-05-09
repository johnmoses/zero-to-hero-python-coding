'''
Tuples search
'''

def search_tuple(data, target):
    for i in data:
        if i == target:
            return data.index(i)
    return 'The element does not exist'

T1 = ('a', 'b', 'c', 'd', 'e')
print(search_tuple(T1, 'c'))