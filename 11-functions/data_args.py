""" 
Any data type including, list, tupple, dictionary can be passed as arguments
"""

def list_args(data):
    for x in data:
        print(x)

fruits = ["apple", "banana", "cherry"]

list_args(fruits)