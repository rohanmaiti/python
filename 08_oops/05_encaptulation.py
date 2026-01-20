# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def printCar(self):
#         print(f'Car brand = {self.brand} and modle = {self.model}')
    

# class ElectricCar(Car):
#     def __init__(self, brand, model, batttery_size):
#         super().__init__(brand, model) # calling parent class constructor
#         self.batttery_size = batttery_size

# my_car = ElectricCar('Toyota', 'Fortuner', '1000kw')
# my_car.printCar()

#* make the brand private and write a another getter method to access that 

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    def get_brand(self):
        print(self.__brand)
    def printCar(self):
        print(f'Car brand is = {self.__brand} and model is {self.model}')

my_car1 = Car('Totyta', 'Fortuner')
# print(my_car1.__brand)
my_car1.get_brand()



# #* Public access:
class User:
    def __init__(self, name):
        self.name = name   # public

u = User("Rohan")
print(u.name)   # allowed

# #* Protected:
# Indicated by single underscore
# Meant for internal / subclass use
class User:
    def __init__(self):
        self._role = "admin"

class Admin(User):
    def show_role(self):
        print(self._role)

a = Admin()
a.show_role()



# #* Private:
# Double underscore
# Python performs name mangling
class User:
    def __init__(self):
        self.__password = "secret"
    def __get_password(self):
        return self.__password
    
    def show_password(self):
        return self.__get_password() 

u = User()
# print(u.__password)  ❌ AttributeError
# Internally becomes: _User__password
# Access (not recommended):
# print(u._User__password)  # works

# ** how make the model instance read only using decorator 
# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand # make this privare 
#         self.__model = model # but has to make this read only 
#     @property
#     def model(self):
#         return self.__model

# my_car = Car('Abc', 'Test')
# print(my_car.brand) #* cant access like this as this is private 
# my_car.model = 'another' #* cant chage as this is read only variabel 
# print(my_car.model)


# #******************************  ***************
# * making setter and getter with 
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):  # getter
        return self.__name

    @name.setter
    def name(self, value):  # setter
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Name must be a string")

p = Person("Rohan")
print(p.name)     # ✅ Calls getter without writing  p.name()

p.name = "Maiti"  # ✅ Calls setter without writing p.set_name()
print(p.name)


