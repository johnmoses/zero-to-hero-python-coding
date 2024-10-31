"""
OOP example
"""
# Define a class
class SharedData:
    spam = 10

    # Constructor
    # def __init__(self, value):
    #     self.spam = value

    # Class method
    def display(self):
        print(self.spam)

# Creating instances
x = SharedData()    # Instance of the class
y = SharedData()    # Another instance

# Accessing attributes
print(x.spam)
print(y.spam)

# Accessing methods
x.display()

# Modifying attributes
SharedData.spam = 80
print(x.spam)
print(y.spam)