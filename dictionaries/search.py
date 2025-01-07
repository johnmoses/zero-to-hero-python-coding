'''
Search Dictionary
'''

dict = {'name': 'Edy', 'age': 26}

def searchDict(d, value):
    for key in d:
        if d[key] == value:
            return key, value
    return 'The value does not exist'
print(searchDict(dict, 26))