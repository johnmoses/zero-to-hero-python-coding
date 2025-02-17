"""
Functions
"""
# Function definition or declaration
def times(x, y):
    return x * y 

# Function call
print('Times: ', times(2,3))

# Saving result to another object
c = times(3, 4)
print('C: ', c)

# Using various types as input parameters
print('Times: ', times('ne', 3))

# Function without parameters
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
print('Add two numbers: ', add_two_numbers())