
class Car:    
    total_car = 0  # This is a class/static variable
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
    def fule_type(self):
        return 'Petrol or Disel'
    def get_brand(self):
        print(self.__brand)
    def printCar(self):
        print(f'Car brand is = {self.__brand} and model is {self.model}')


class ElectricCar(Car):
    def __init__(self, brand, model, batttery_size):
        super().__init__(brand, model)
        self.batttery_size = batttery_size
    def fule_type(self):
        return 'Electric power'


my_petrol_car = Car('Honda', 'I20')
my_electric_car = ElectricCar('Tesla', 'M1', '2000kw')
print(my_petrol_car.fule_type())
print(my_electric_car.fule_type()) # it overwrites the same_method, so ans --> Electric power
# #* above is compile time 


# # ******** Example -2 
# class Cat:
#     def speak(self): return "Meow"

# class Dog:
#     def speak(self): return "Bark"

# def animal_sound(animal):
#     print(animal.speak())

# animal_sound(Dog())
# animal_sound(Cat())


# ** checking how to create a static variable 
# my_petrol_car = Car('Honda', 'I20')
# my_petrol_car = Car('Honda', 'I20')
# my_petrol_car = Car('Honda', 'I20')
# print(Car.total_car)


