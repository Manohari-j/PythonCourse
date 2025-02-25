# Have many forms
# 2 ways :
# 1.Inheritance - an obj could be treated of the same type as a parent class
# 2.Duck Typing - Obj must have necessary attr/methods

# for abstract classes
import math
from abc import ABC, abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle): # an obj can be treated of same type as parent
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


# list of objects

shapes = [Circle(5), Square(5), Triangle(3, 6), Pizza("Cheese", 15)]

# print(shapes[0].area())
# print(shapes[1].area())
# print(shapes[2].area())

for shape in shapes:
    print(f"Area is {shape.area():.2f}sq.cm")
