# another way to achieve polymorphism. obj must have min attr/methods
# "If it looks like a duck and quacks like a duck, it must be a duck"


class Animal:
    alive = True
    # def __init__(self, name):
    #     self.name = name
    #     self.is_alive = True
    #
    # def eat(self):
    #     print(f"{self.name} is eating")
    #
    # def sleep(self):
    #     print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("WOOF, WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW, MEOW!")


class Car: # it has min attr/methods
    alive=False
    def speak(self):
        print("Honk!")


animals = [Dog(), Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Mickey")
#
# dog.sleep()
# mouse.eat()
# cat.speak()
