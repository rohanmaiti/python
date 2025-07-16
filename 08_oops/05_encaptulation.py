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
