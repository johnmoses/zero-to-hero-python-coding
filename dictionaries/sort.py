'''
Sort a dictionary
'''

dic = {'name': 'Peter', 'height': 4, 'complexion': 'fair', 'sex': 'male' }
print('Data: ', dic)

# Basic
print('Basic: ', sorted(dic))

# Sort by key
print('By key: ', sorted(dic.items()))

# Sort by value
print('By value: ', sorted(dic.items(), key=lambda x : x[0]))