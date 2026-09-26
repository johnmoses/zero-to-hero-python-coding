""" 
Dictionary comprehension
"""

numbers = {i: i for i in range(1, 10)}
print('Numbers: ',numbers)

even_numbers = {i: i for i in range(1, 10) if i % 2 == 0}
print('Even numbers: ',even_numbers)

squares = {i: i ** 2 for i in range(1, 10)}
print('Squares: ', squares)