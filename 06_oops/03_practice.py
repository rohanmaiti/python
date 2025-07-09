# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programmer:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

no_of_employee = 10
employeeList = []
for i in range(0, no_of_employee):

