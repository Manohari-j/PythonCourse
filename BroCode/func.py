# function: A block of reusable code
# 1. Positional: hello(fname,lname) - arg is positional, if changed will mean diff
# 2. Default: used when arg is omitted. fill up from right
# 3. Keyword: arg preceded by an id. order of args doesn't matter
# hello(fname = "Manohari",lname = "Jayachandran") def hello(lname,fname)
# will work correctly. but positional arg first and then kw arg. fill up from right
# end/sep in print st is KW arg. replacing the /n with other

print("1", "2", "3", "4", "5", sep='-')


# 4. Arbitrary args: Varying amount of args *unpacking operator
# *args: allows you to pass multiple non key args
# **kwargs: allows you to pass multiple keyword arguments

def add(*args):  # can be *nums or any name. * is important as it unpacks the args
    # print(type(args)) # tuple
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3, 4))


def print_addr(**kwargs):
    # print(type(kwargs)) # dictionary
    for k, v in kwargs.items():
        print(f"{k:7}:{v}")


print_addr(street="365 Neville Drive", city="Grayslake", state="Illinois", zip="60030")

# mix of args and kwargs

def shipping(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for k, v in kwargs.items():
    #     print(f"{k:7}:{v}")
    print(f"{kwargs.get('street')}, {kwargs.get('apt')}")
    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('state')} - {kwargs.get('zip')} ")

shipping("Mrs.","Manohari","Jayachandran",street="365 Neville Drive", apt="#4", city="Grayslake", state="Illinois", zip="60030")
