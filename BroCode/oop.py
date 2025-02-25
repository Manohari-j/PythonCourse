# Object = A bundle of related attr/var and methods/fns
# you need a class to create many objects
# class: blueprint used to design the structure and layout of an object

# dunder __init__ is a constructor method to initialise the attributes and to create an object


from car import Car

c1 = Car("Tesla", 2025, "White", False)
c2 = Car("BMW", 2025, "Blue", False)
c2 = Car("Charger", 2009, "Red", True)

print(c1.model)  # . is attribute access operator
print(c2.model)
c1.drive()
c2.stop()
c1.describe()
c2.describe()

# better pracice is to access the class var using class name rather than object var
print(f"{c1.model} has {Car.wheels} wheels")
print(f"{c2.model} has {Car.wheels} wheels")
print(f"Total number of cars : {Car.num_of_cars}")
