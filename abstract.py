# abc is file from ABC class import abstract method

from abc import ABC, abstractmethod

# abs method don't allow to instantiate an obj for the class
# forces the child class to create an object
# now to make a class abstract inherit it from ABC class
class Vehicle(ABC):  # abstract: inheriting classes define the func. Don't allow creation of object for this class
    @abstractmethod # decorator, so python interpreter understands this is abs method
    def start(self):
        pass

# classes inheriting abs class must override all abs method

# passing objects
# In Python all var are public.
# Dunder var/methods: To make it private use __pwd, __variable, --method too....
# To make it protected use _variable_name, _method_name
# __name__ : Internal var/methods of python
class Bike(Vehicle):  # concrete class
    color = None

    def start(self):
        print("You are riding a bike")


class Car(Vehicle):
    color = None


    def start(self):
        print("You are riding a car")
