# Decorator: A function that extends the behavior of another function
# without modifying the base function
# pass the base function as an arg to the decorator
# to add emoji Press the Windows key and the period (.) key simultaneously

# decorator
# wrapper is required else this func is automatically called as soon as it hits @
# func with arg means wrapper will have args and kwargs
# to accept any number of args and key word args
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🎊*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge 🍫")
        func(*args, **kwargs)
    return wrapper
# def add_sprinkles(func):
#     print("*You add sprinkles 🎊*")
#     func()


@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your {flavor} Ice Cream 🍨")

# get_ice_cream()
get_ice_cream("Vanilla")