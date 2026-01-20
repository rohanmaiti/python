# Python provides abstraction using:
# ABC (Abstract Base Class)
# @abstractmethod

# #* Basic abstract class example
from abc import ABC, abstractmethod
class Vehical(ABC): 
    @abstractmethod
    def start():
        pass

    @abstractmethod
    def stop(self):
        pass

"""
Vehicle cannot be instantiated
start() has no implementation
Child class must implement start() and stop(). Else If one is missing → TypeError
"""

# #* Implementing abstract class
class HondaCar(Vehical):
    def start():
        print(f"Honda car starts broom broom")

car = HondaCar()
car.start()

# #* Abstract class CAN have concrete methods
class Vehicle(ABC):

    def fuel_type(self):
        return "Petrol"

    @abstractmethod
    def start(self):
        pass


# #* Interface
# Python has no real interface keyword
# We simulate it using only abstract methods