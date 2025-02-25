# @property: Decorator used to define a method as a property(can be accessed like an attribute)
# add additional logic, gives getter, setter and deleter method
# _ before an attr means private

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property  # to access private attr
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height

    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height deleted")


r = Rectangle(3, 4)

r.width = 10
r.height = 69
print(r.width)
print(r.height)
del r.width
del r.height

# print(r.width)
# print(r.height)

