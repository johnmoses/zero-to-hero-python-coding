""" 
Join or concatenate lists
"""

numbers = [1, 2, 3, 4, 5]
subjects = ['physics', 'chemistry', 'biology']
fruits = ['banana','apple']

joined_list = numbers + subjects
print(joined_list)

extended_list = numbers.extend(subjects)
print(extended_list)