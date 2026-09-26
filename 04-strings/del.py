# del 
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits) 
del fruits[0]     
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]     
print(fruits)       # ['orange', 'lemon']
del fruits      # This should give: NameError: name 'fruits' is not defined
# print(fruits) 