""" 
Recursive Function

Write a simple recursive function
"""
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
countdown(5)