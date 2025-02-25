# static method: A method that belongs to a class rather than any object from thatclass
# 1. Instance method(self): Best for operation on instances of the class
# 2. Static methods(): Best for utility functions that do not need access to class data
# 3. Class Methods(cls): Allow operations related to the class itself.
# take CLS as the first param, which represent the class itself
# 4. Magic Methods: Dunder methods __init__, __str__, __eq__
# automatically called by many of built in oper. used to define/ customize the behavior of objects
class Employee:

    def __init__(self, name, position):
        self.name =name
        self.position =position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Software Engineer", "Project Manager", "Principle Architect"]
        # for pos in valid_positions:
        #     if pos == position:
        #         return True
        # return False

        return position in valid_positions



e1=Employee("Mano", "Software Engineer")
print(e1.get_info())
print(Employee.is_valid_position("Project Manager"))


# class method

class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=1
        Student.total_gpa += gpa

    #Instance method
    def get_info(self):
        return f"{self.name} = {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total num of students: {cls.count}"
    @classmethod
    def get_gpa(cls):
        if cls.count == 0:
            return 0
        return f"Average gpa of students: {cls.total_gpa/cls.count :.2f}"


s1 = Student("Jai", 4.0)
s2 = Student("Subhi", 4.6)
s3 = Student("Madhav", 4.5)

print(Student.get_count())
print(Student.get_gpa())