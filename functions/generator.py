""" 
Generator Functions

These are functions that return a lazy iterator. These are objects that you can iterate over like a list. 
However, unlike lists, lazy iterators do not store their contents in memory.
"""
def generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    
for i in generator():
    print(i)

