s = 'Spam'

# Analysing
print('Analysing')
print(len(s))

# Indexing
print('Indexing')
print(s[0])           # index of first element
print(s[1])          # index of second element
print(s[-1])   # last item from end

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) 
# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) 


# Repeat
print(s * 2)

s = 'z' + s[1:]
print(s)

# Expanding to list
print('Expanding with list')
l = list(s)
print(l)

# Subset
print('Subsets')
fs = s.find('pa')
print(fs)
