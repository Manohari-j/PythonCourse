# built-in functions
# arg/parameters - () or (value), return value
# print("Hello")
# num = input("Enter a number:")

# def greet(name):
#     """ docstring: describes what the function does """
#     print("Hello " + name)
#
#
# greet(name="Jai") #keyword argument
#
# # sum of n natural numbers
#
# def sum(n):
#     return n*(n+1)/2
#
#
# print(sum(3))
#
# # variable scope - global, local
#
# num=10
# def printn():
#     global num  # declaring num as global
#     num=20
#     print(num)
#
# printn()
# print(num)
#
#
# # variable length arguments *args receives as tuples
#
# def sum_total(*vals):
#     sum =0
#     for i in vals:
#         sum += i
#     return sum
#
#
# print(sum_total(3,4,5,6,7,8))

# keyword argument ** packs all kwargs into a dictionary

def addr(**keyvalue):
    for k,v in keyvalue.items():
        print(v)

addr(door=365, street="Neville Drive", Apt=4, city="Grayslake", state="Illinois")


# default argument : fill it up from left. if left is given default...follow all args with default

def add(a,b=30):
    return a+b


print(add(40))

# Passing list
def print_list(prog):
    for p in range(0, len(prog)):
        prog[p]=prog[p].title() # to change in the original list assign to it
        # to avoid it use[:]
        print(prog[p]) # capitalise first letter

    # for p in prog:
    #     print(p.title()) # capitalise first letter


program=["C","C++","javaScript","python"]
print_list(program[:]) # it changes the .title permanently
print(program)


# returning dictionary

def user_info():
    user={'name':'Mano', 'age': 39}
    return user

user=user_info()
print(user)


# Modules: only one is main and all others are modules which has func/classes
# Similar jobs/fns are written in one module
