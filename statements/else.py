""" 
else statement
"""

a = 300
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short hand
print("b is greater") if b > a else print("a is greater")

# Handling many conditions
print("b is greater") if b > a else print("=") if a == b else print("a is greater")