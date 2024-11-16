""" 
Dates
"""

import datetime

x = datetime.datetime.now()
print(x)

# Get year
print(x.year)

# Get weekday
print(x.strftime("%A"))

# Creating dates
x = datetime.datetime(2020, 5, 17)

print(x)