# class var are shared among all instances of a class
# defined outside the constructor.
# Allow to share data among all obj created from that class

class Car:
    wheels = 4  # class variables
    num_of_cars = 0

    def __init__(self, model, year, color, for_sale):
        self.model = model  # Instance Variables
        self.year = year
        self.color = color
        self.for_sale = for_sale
        Car.num_of_cars +=1

    def drive(self):
        print(f"you drive the {self.color} {self.model}")

    def stop(self):
        print(f"you stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
