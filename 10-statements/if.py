"""
if statement
"""

# Short hand if statement
a = 40
b = 6
c = 50
if a > b: 
    print("a is greater than b")

# Using 'and' condition
if a > b and c > a:
  print("Both conditions are True")

# Using 'or' condition
if a > b or a > c:
  print("At least one of the conditions is True")

# Using 'not' condition
if not a > b:
    print("a is NOT greater than b")

# Nested
if a > 10:
    print("Above ten,")
    if a > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# Multiline if statement
var = int(input("Enter integer value: "))
if var == 1:
    print('Turning up!')
    print(var)

if var == 0:
    print('shutting down!')
    print(var)

print('Good bye!')