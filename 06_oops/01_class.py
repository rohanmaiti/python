
#* Creating a class in python
#* Note the class name is starting with capital letter
class Myclass:
    name='Rohan'
    age=21
#* Create Object
# Now we can use the class named MyClass to create objects:
obj = Myclass()
# print(obj.name)
# print(obj.age)


# ****************************************************

#* Class attriubtes and instance attributes
class Car:
    noOfWheel = 4 # this is class attrubute

inova = Car()
inova.noOfWheel = 10 # this is an instance attribute
inova.color = 'red'
# print(inova.color, inova.noOfWheel)

# ****************************************************
class Employee:
    name='Rohan'
    salary=120000
    def getInfo(self):
        print(f'Employee name {self.name} and salary {self.salary}')

emp1 = Employee()
emp1.getInfo()
# the above line is being called like this --> Employee.getInfo(emp1); 
# that's why need to accept a argument at the function defination
# every function in the function defination in a class need to write one argument "MUST"






