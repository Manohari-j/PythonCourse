# Allows a class to inherit attr and methods from another class
# code reusability and extensibility

# class Father:
#     height =182
#     color = "pink"
#
# class Son(Father):
#     pass

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
#
#     def eat(self):
#         print(f"{self.name} is eating")
#
#     def sleep(self):
#         print(f"{self.name} is sleeping")
#
#
# class Dog(Animal):
#     def speak(self):
#         print("WOOF, WOOF!")
#
#
# class Cat(Animal):
#     def speak(self):
#         print("MEOW, MEOW!")
#
#
# class Mouse(Animal):
#     def speak(self):
#         print("Squeak, Squeak!")
#
#
# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Mickey")
#
# dog.sleep()
# mouse.eat()
# cat.speak()

# Multiple Inheritance: Inherit from more than one parent class C(A,B)
# Multilevel Inheritance: Inherit from a parent which inherits from another parent
# C(B)<-B(A)<-A
class Animal:
    def __init__(self,name):
        self.name = name


    def eat(self):
        print(f"{self.name}  is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


r = Rabbit("Bugs")
h = Hawk("Tony")
f = Fish("Nemo")

r.flee()
h.hunt()
f.flee()
f.hunt()
r.eat()
f.sleep()
h.eat()
