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


# is there multiple inheritance in python ?
class Battery:
    def __init__(self, brand):
        self.brand = brand
    def print_battery(self):
        return self.brand
   
class Engine:
    def __init__(self, engine):
        self.engine = engine
    def print_engine(self):
        return self.engine
    

class Car(Battery, Engine):
    def __init__(self, battery, engine):
        Battery.__init__(self, battery)   # ✅ Explicitly call Battery constructor
        Engine.__init__(self, engine)   # ✅ Explicitly call Engine constructor

my_car = Car('1000kw', 'tata')
print(my_car.print_engine())
print(my_car.print_battery())