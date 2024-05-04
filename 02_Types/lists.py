# Lists

list1 = ['abcd', 785, 2.23, 'john', 70.2]
list2 = [123, 'john']
list3 = ['physics', 'chemistry', 'biology']
list4 = [1, 2, 3, 4, 5]
list5 = ['a', 'b', 'c', 'd']

# Accessing values
print(list1)             #complete list
print(list2)         #complete second list

print(list2 * 2)     #two times
print(list1 + list2)  #concatenated

# Indexing
print(list3.index('biology'))

print(list3[0])          #first element
print(list3[1:3])        #start from second till third
print(list3[2:])         #start from third

# Searching
def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value was not found'
print(searchinList(list4, 3))

# Updating values
print(list4)
list4[4] = 50
print(list4)

# Inserting new values
list3.insert(0, 'Religion')
print(list3)

# Poping from lists
list3.pop()
print(list3)
list3.pop(1)
print(list3)

# Removing from lists
list3.remove('chemistry')
print('Remove: ',list3)

# Reversing lists
list4.reverse()
print('reverse: ',list4)

# Deleting from list
del list4[3]
print('List 4 with delete: ',list4)

# Appending to lists
print('List 3: ',list3)
list3.append('Civics')
print('Append: ', list3)

# Sequence operations
print('list4 length: ',len(list4))
print('list4 max: ',max(list4))
print('list4 min: ',min(list4))

