"""
Simple Python Class
"""
# Define a class
class SharedData:
    spam = 10

# Creating instances
x = SharedData()    # Instance of the class
y = SharedData()    # Another instance

# Accessing attributes
print(x.spam)
print(y.spam)

# Modifying attributes
SharedData.spam = 80
print(x.spam)
print(y.spam)