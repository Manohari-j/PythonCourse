# from script2 import *

# print(dir()) # attributes
# print

def fav_food(food):
    print(f"Your favorite food is {food}")


def main():
    print("This is script1")
    fav_food("Dosa")
    print("Goodbye!")


# I want to run this code only if it is run directly
# if it is imported and run in script2, these codes will not be executed
if __name__ == '__main__':
    main()
