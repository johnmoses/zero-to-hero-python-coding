""" 
Tuple comprehension
"""

numbers = (i for i in range(1, 100))
print('Numbers: ')
for i in numbers:
    print(i, end=' ')