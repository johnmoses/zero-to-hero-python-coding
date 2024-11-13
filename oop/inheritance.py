""" 
Inheritance
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
