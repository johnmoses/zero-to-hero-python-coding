""" 
Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
"""

class Student:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_names(self):
        print(self.firstname, self.lastname)

student = Student("John", "Doe")
student.print_names()

class Graduant(Student):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

graduant = Graduant("John", "Happy", 2019)
graduant.welcome()
