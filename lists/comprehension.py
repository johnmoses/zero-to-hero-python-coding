""" 
List comprehension
"""

# Listing single numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers) 

# List tuples of numbers
numbers = [(i, i * i) for i in range(11)]
print(numbers)   

# Even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)  

# Odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)  

# Flattening a multidimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list) 