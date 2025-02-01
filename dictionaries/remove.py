""" 
Remove item from dictionary
"""

dict = {'name': 'Edy', 'age': 26, 'phone':'08023344334'}

# Remove first key
dict.pop('name')
print(dict)

# Remove last item
dict.popitem()
print(dict)