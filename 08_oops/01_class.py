
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

#* Class attriubtes vs instance attributes
class Car:
    noOfWheel = 4 # this is class attrubute

inova = Car()
inova.noOfWheel = 10 # this is an instance attribute
inova.color = 'red'
# print(inova.color, inova.noOfWheel)

class Car:
    wheels = 4  # Class variable (shared by all instances)
    
    def __init__(self, name, color):
        self.name = name     # Instance variable
        self.color = color   # Instance variable

# *******************   SELF    *********************************
# class Employee:
#     name='Rohan'
#     salary=120000
#     def getInfo(self):
#         print(f'Employee name {self.name} and salary {self.salary}')

# emp1 = Employee()
# emp1.getInfo()
# *the above line is being called like this --> Employee.getInfo(emp1); 
# that's why need to accept a argument at the function defination
# every function in the function defination in a class need to write one argument "MUST"

# ***************************
#* Instance vs Class Variables
# class Counter:
#     count = 0   # class variable
#     def __init__(self):
#         Counter.count += 1  # modifies class variable
#         self.id = Counter.count  # instance variable


# ****************************
#*  Instance / Class / Static Methods
class Demo:
    def instance_method(self):
        print("Called instance method", self)

    @classmethod
    def class_method(cls):
        print("Called class method", cls)

    @staticmethod
    def static_method():
        print("Called static method")

d = Demo()
d.instance_method()
Demo.class_method()
Demo.static_method() 
d.static_method()



"""
Feature	                     Instance Method	      Class Method	        Static Method
Decorator	                    None	             @classmethod	    @staticmethod
First Parameter	             self (instance)	     cls (class)	          None
Call via Instance	         ✅ obj.method()	        ✅ obj.method()	    ✅ obj.method()
Call via Class	             ❌ (needs instance)	    ✅ Class.method()	✅ Class.method()
Access Instance Variables	 ✅ Yes	                ❌ No	            ❌ No
Modify Instance State	     ✅ Yes	                ❌ No	            ❌ No (unless passed)
Access Class Variables	     ✅ Yes	                ✅ Yes	            ❌ No (unless passed)
Modify Class State         	 ✅ Yes	                ✅ Yes	            ❌ No
Use Case	            Work with object data	    Factory methods,     modify class state	Utility functions
"""


class Demo:
    count = 0  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
    
    @staticmethod
    def modify_instance(instance, new_name):
        # ✅ Can modify instance variable if instance is passed
        instance.name = new_name
        print(f"Modified instance variable: {instance.name}")
    
    @staticmethod
    def modify_class(cls, new_count):
        # ✅ Can modify class variable if class is passed
        cls.count = new_count
        print(f"Modified class variable: {cls.count}")

# Create instance
d = Demo("Rohan")
print(d.name)  # Output: Rohan

# Modify instance variable via static method
Demo.modify_instance(d, "Rahul")
print(d.name)  # Output: Rahul

# Modify class variable via static method
print(Demo.count)  # Output: 0
Demo.modify_class(Demo, 10)
print(Demo.count)  # Output: 10


# #* How on method call another method inside a class ?
class Calculator: 
    def __init__(self, value): 
        self.value = value
    def add(self, num):
        self.value += num
        return self.value    
    def multiply(self, num): 
        self.value *= num
        return self.value
    def add_and_multiply(self, add_num, multi_num):
        self.add(add_num)
        self.multiply(multi_num)
        return self.value

calc = Calculator(10)
result = calc.add_and_multiply(10, 20)
print(f"result is = {result}")