""" 
Function as parameter
"""

def sum_numbers(nums):
    return sum(nums)

def function_as_parameter(fn, nums):
    summ = fn(nums)
    return summ

nums = [1, 2, 3, 4, 5]
print(function_as_parameter(sum_numbers, nums))