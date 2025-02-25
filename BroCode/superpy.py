# super(): Function used in a child class to call methods from a parent class
# allows you to extend the functionality of the inherited methods
# method overriding
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"Circle is {self.color} and {'filled' if self.is_filled else 'not filled'} and has {self.radius}cm radius")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"Square is {self.color} and {'filled' if self.is_filled else 'not filled'} and has {self.width}cm width")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"Triangle is {self.color} and {'filled' if self.is_filled else 'not filled'} and has {self.width}cm width and {self.height}cm height")

c=Circle("red", True, 5)
t=Triangle("blue", False, 8,8)
s=Square("Yellow", True, 5)

print(c.color)
c.describe()
t.describe()
s.describe()