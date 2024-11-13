""" 
Arbitrary argumennts have '*' before the arg name in the function definition
The arguments are stored as tuple
"""

def arbitrary_args(*fruits):
      print(fruits)

arbitrary_args("Orange", "Mango", "Avocado","Almond")

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num 
    return total
    
print(sum_all_nums(2, 3, 5, 1, 2)) 