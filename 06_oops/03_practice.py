# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.
# class Programmer:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# no_of_employee = 3
# employeeList = []
# for i in range(0, no_of_employee):
#     name = input("Enter employee name : ")
#     salary = input("Enter employee salary : ")
#     newEmp = Programmer(name, salary)
#     employeeList.append(newEmp)
# else:
#     print('---Details of employee---')
#     for emp in employeeList:
#         print(emp.name, '--', emp.salary)


# Write a class “Calculator” capable of finding square, cube and square root of a
# number.
import math
class Calculator:
    @staticmethod
    def square(num):
        return num * num
    def cube(num):
        return num*num*num
    def squareroot(num):
        return  math.sqrt(num)
    @staticmethod
    def hello():
        print('Hello user')

print(Calculator.square(10))
print(Calculator.cube(10))
print(Calculator.squareroot(10))
Calculator.hello()

# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

class Train:
    allStations = {
        stations: [
            {
                name: 'Balichak',
                id:'1'
            },
            {
                name: 'Samchak',
                id:'2'
            },
            {
                name: 'Madpur',
                id:'3'
            },
            {
                name: 'Kharagpur',
                id:'4'
            },
            {
                name: 'Medinipur',
                id:'5'
            }
        ]
    }
    @staticmethod
    def calcualteFare(source, destination):
            for station in allStations.stations:
                if ( source == station.name ):
                    s = station.name
                if (destionation == station.name):
                    d = station.name
        
            if ( s == None or d == None) :
             print('Enter valid stations name')
            else:
             print('Your fare is')