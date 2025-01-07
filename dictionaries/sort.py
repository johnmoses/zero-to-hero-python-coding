'''
Sort a dictionary
'''

dict = {'name': 'Peter', 'height': 4, 'complexion': 'fair', 'sex': 'male' }
print('Data: ', dict)

# Basic
print('Basic: ', sorted(dict))

# Sort by key
print('By key: ', sorted(dict.items()))

# Sort by value
print('By value: ', sorted(dict.items(), key=lambda x : x[0]))