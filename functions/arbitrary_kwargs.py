""" 
Arbitrary keyword argumennts have '**' before the arg name in the function definition
The arguments are stored as a dictionary
"""

def arbitrary_kwargs(**details):
      print(details)

arbitrary_kwargs(name="Joy", age="16")