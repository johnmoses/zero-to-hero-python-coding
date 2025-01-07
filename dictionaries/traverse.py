""" 
Traverse
"""

dict = {'name': 'Edy', 'age': 26}

def traverseDict(d):
    for key in d:
        print(key, d[key])

traverseDict(dict)