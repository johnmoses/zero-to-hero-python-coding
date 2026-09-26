"""
Functions
"""
# Function definition or declaration
def times(x, y):
    return x * y 

# Function call
print('Multiply two numbers: ', times(2,3))

# Saving result to another object
c = times(2,3)
print('Result in another object: ', c)

# Using various types as input parameters
print('Multiply text: ', times('ne', 3))

# Function without parameters
print('No parameters: ')
def generate_full_name ():
    first_name = 'John'
    last_name = 'Mark'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()

# Returning a value
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print('Return value: ', add_two_numbers())