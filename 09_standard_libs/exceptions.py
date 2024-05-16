"""
Exception example
"""

def reader(obj, index):
    return obj[index]

def catcher(obj, index):
    try:
        print(reader(obj, index))
    except IndexError:
        print('Got exception')
    print('Reading!')

x = 'Rain'
print(reader(x, 2)) # Works well
# print(reader(x, 5)) # Throws IndexError exception
catcher(x, 5)