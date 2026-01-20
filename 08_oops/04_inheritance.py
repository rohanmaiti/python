class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def printCar(self):
        print(f'Car brand = {self.brand} and modle = {self.model}')
    

# #* 1. Signle inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, batttery_size):
        super().__init__(brand, model) # calling parent class constructor
        self.batttery_size = batttery_size

my_car = ElectricCar('Toyota', 'Fortuner', '1000kw')
my_car.printCar()


# #* 2. Multiple inheritance (Multiple parents, one child	) in python ? --> yes
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


# #* If battery and Engine class both have same function name then what will happen ?
# #* Python follows MRO (Method Resolution Order).
# Left-to-right inheritance order matters
# First matching method is called
class Battery:
    def start(self):
        print("Battery start")

class Engine:
    def start(self):
        print("Engine start")

class Car(Battery, Engine):
    pass

c = Car()
c.start()

print(Car.__mro__)

# There is also 3. Multilevel inheritance (Chain A→B→C), 4. Hyerachial inheritance (One parent, multiple children), 5. Hybrid inheritance  (mix)