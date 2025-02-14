# class is defined in user.py

# from user import User, Student, Faculty, TempFaculty
# from user import *
from abstract import *

# u1 = User("Jai", "we123")  # calls init method automatically
# u2 = User("Madhav", "6er66")
# u3 = User("Subhi", "333ab")
#
# u1.register() # encapsulation. fn called with obj, self indicates the obj
# u2.login()
# print(u1.user_name)
# print(u3.pwd)
# print(User.users)

# users var behaves different than static because it can be used with
# object variable as well as class name whereas static can be linked only with class
# but avoid it with obj var
# u1.users = 10
# User.users =100
# print(u1.users)
# print(User.users)

# s1=Student()
# f1=Faculty()
# t1=TempFaculty()
# st1=StudentFaculty()
# u1=User()
# s1.greet_student()
# f1.greet_faculty()
# s1.login()
# t1.greet_faculty()
# t1.greet_temp_faculty()
# st1.greet_student()
# st1.greet_faculty()
# st1.register()


# s1.greet()
# f1.greet()
# t1.greet()
# st1.greet()
# u1.greet()

# method chaining

# u1.login().greet()  # throws error if login is not returning an object - self

# s1=Student("Mano","123wer","CSE",100000)
# s1.greet_student()
# sf1 = StudentFaculty("Jai","abc345","ME",300000)
# sf1.greet()

# c1 = Car()
# c1.start()
# # before making it as abstract
# v1=Vehicle()
# v1.start()

def set_color(veh,color):
    veh.color = color
    veh.start()
# Duck typing: Importance to methods than the objects
# In C++/Java it takes only particular obj, but here any obj is accepted hence duck typing
c1=Car()
b1=Bike()

set_color(c1,"blue")
set_color(b1,"red")

print(c1.color)
print(b1.color)






