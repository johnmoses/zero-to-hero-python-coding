""" 
Employee class example
"""

class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, "does many things")

    def __repr__(self):
        return "Employee: name=%s, salary=%s" % (self.name, self.salary)

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, "cooks food")

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 4000)

    def work(self):
        print(self.name, "serves food")

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, "makes pizza")

if __name__ == "__main__":
    rex = PizzaRobot('Rex')
    print(rex)
    rex.work()
    rex.giveRaise(0.3)
    print(rex)

    # Print work
    print('Summary')
    for cl in Employee, Chef, Server, PizzaRobot:
        obj = cl(cl.__name__)
        obj.work()