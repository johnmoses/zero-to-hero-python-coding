"""
Composition

Composition means building a class by including instances of other classes
as attributes, rather than inheriting from them.

Rule of thumb:
  - Use inheritance for "is-a" relationships  (Dog IS-A Animal)
  - Use composition for "has-a" relationships (Car HAS-A Engine)
"""

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine ({self.horsepower}hp) started")

    def stop(self):
        print("Engine stopped")


class Car:
    """Car HAS-A Engine — composition, not inheritance."""
    def __init__(self, make, horsepower):
        self.make = make
        self.engine = Engine(horsepower)   # Engine is a component of Car

    def drive(self):
        self.engine.start()                # delegate to the component
        print(f"{self.make} is driving")

    def park(self):
        self.engine.stop()
        print(f"{self.make} is parked")


car = Car("Toyota", 150)
car.drive()
car.park()