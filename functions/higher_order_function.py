""" 
Higher Order Functions
"""

def higher_order_function(type):
    if type == 'square':
        return 'square'
    elif type == 'circle':
        return 'circle'
    elif type == 'rectangle':
        return 'rectangle'

print(higher_order_function('square'))
print(higher_order_function('circle'))
print(higher_order_function('rectangle'))