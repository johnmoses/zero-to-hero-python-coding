""" 
Enclosure
"""

def add_nums():
    first = 10
    def add (num):
        return num + first
    return add

print(add_nums())