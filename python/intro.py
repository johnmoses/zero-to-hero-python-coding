"""
Simple Python program
"""

print('Hello World!')

# Print numbers 0-9
for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)

# Do some calculations
for i in range(10):
    x = i*0.1
    print(x)
    print(x/(1-x*x))

# Indentation
if 5 > 2:
  print("Five is greater than two!")

# Variables
x = 5
y = "Hello, World!"
print(x)
print(y)