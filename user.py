class User:
    # user_name = None
    # pwd = None

    # class variables like static var
    users = 0  # belongs to class

    # To initialise the variable like constructors
    # self is like 'this' . it indicates the obj calling the method
    def __init__(self, user_name,pwd):
        self.user_name = user_name # instance variable : object's variable
        self.pwd = pwd
        User.users +=1 # class var has to be called with class name

    def register(self):
        # print("Registering " + self.user_name)
        print("Registering ")

    def login(self):
        # print("Logging in "+ self.user_name)
        print("Logging in")
        return self

    def greet(self):
        print("Hello, user")

        # Inheritance
        # method overriding using greet method
# Super to access parent class method
class Student(User):
    def __init__(self,user_name,pwd, course, fee):
        super().__init__(user_name,pwd) # super fn init base obj
        self.course = course
        self.fee = fee

    def greet_student(self):
        super().greet()
        print("Hi Student")
        print("Name: " + self.user_name)
        print("Pwd: " + self.pwd)
        print("Course: " + self.course)
        print("Fee: " + str(self.fee))

    def greet(self):
        print("Hello, Student")


class Faculty(User):

    def greet_faculty(self):
        print("Hello Teacher")
    def greet(self):
        print("Hello, Teacher")


class TempFaculty(Faculty):  # multilevel inheritance

    def greet_temp_faculty(self):
        print("Hello, welcome")
    def greet(self):
        print("Hello, welcome")


# multiple: one class inheriting from more than one class
class StudentFaculty(Student, Faculty):
    # pass  # to pass the definition

    def greet(self):
        super().greet()
        print("Hello, student faculty")
