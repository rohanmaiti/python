
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
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
print(my_electric_car.fule_type())