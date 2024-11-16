""" 
F-String formatting
"""
txt = f"The price is 50 dollars"
print(txt)

# Using modifier by adding ':' followed by type
price = 60
txt = f"The price is {price:.2f} dollars"
print(txt)

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

# Doing calculations
txt = f"The price is {5 * 8} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

# Include conditional statements
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

# Execute functions
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

# Using placeholders
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Named indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))