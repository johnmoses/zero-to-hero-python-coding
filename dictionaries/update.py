""" 
Update
"""

dict = {'name': 'Edy', 'age': 26}

print('Method 1')
dict['address'] = 'London'
print(dict)

print('Method 2')
dict.update({'name':'Vicky'})
print(dict.items())