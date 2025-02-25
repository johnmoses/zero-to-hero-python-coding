""" 
Composition
"""

# Component class
class Component: 
	def __init__(self): 
		print('Component class object created...') 

	def m1(self): 
		print('Component class m1() method executed...') 

# Composite class
class Composite: 
	def __init__(self): 
		self.obj1 = Component() 
		
		print('Composite class object also created...') 

	def m2(self): 
		
		print('Composite class m2() method executed...') 

		self.obj1.m1() 

obj2 = Composite() 
obj2.m2() 
