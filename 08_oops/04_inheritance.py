class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def printCar(self):
        print(f'Car brand = {self.brand} and modle = {self.model}')
    

class ElectricCar(Car):
    def __init__(self, brand, model, batttery_size):
        super().__init__(brand, model) # calling parent class constructor
        self.batttery_size = batttery_size

my_car = ElectricCar('Toyota', 'Fortuner', '1000kw')
my_car.printCar()