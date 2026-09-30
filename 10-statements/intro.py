"""
Simple Python statement
"""

# Check if b is greater than a
a = 33
b = 200
if b > a:
  print("b is greater than a")

# Check if user enters 'stop'
while True:
    reply = input("Enter text: ")
    if reply == 'stop': 
          break
    print(reply)