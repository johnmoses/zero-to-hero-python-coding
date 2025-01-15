""" 
Dates
"""

import datetime

x = datetime.datetime.now()
print('Now: ', x)

# Get year
print('Year: ', x.year)

# Get month
print('Month: ', x.month)

# Get day
print('Day: ', x.day)

# Get hour
print('Hour: ', x.hour)

# Get minute
print('Minute: ', x.minute)

# get second
print('Second: ', x.second)

# Get timestamp
print('Timestamp: ', x.timestamp)

# Get weekday
print(x.strftime("%A"))

# Creating dates
x = datetime.datetime(2020, 5, 17)
print('Date: ', x)