""" 
Class example
"""

# Define a class
class MixedNames:
    data = 'spam'

    # Define a constructor method
    def __init__(self, value):
        self.data = value

    # Define another method
    def display(self):
        print(self.data, MixedNames.data)

# Creating instances
x = MixedNames(1)
y = MixedNames(2)

# Calling methods
x.display()
y.display()