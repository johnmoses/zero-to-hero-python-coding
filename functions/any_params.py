"""
Any number of parameters
"""

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num 
    return total
print(sum_all_nums(2, 3, 5, 1, 2)) 