#* Static method 
class Employee:
    @staticmethod
    def printHello():
        print("Hello from employee")

Employee.printHello()
# or 
emp1 = Employee()
emp1.printHello()


class Car:
    def __init__(self, name, color):   #* dunder method ( methods starts with __ )
        self.name = name 
        self.color = color

car1 = Car('inova', 'red')
print(car1.name, car1.color)
