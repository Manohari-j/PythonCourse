import random

# print(__name__)  # __main__ is the output
# if this module is called from another file, then name will have the name that calls this module
# This condn can be used if any part of the prog need not be executed while called from elsewhere.
if __name__ == '__main__':
    print("You are running this directly")
num = random.randint(1, 20)
attempts = 0
guess = int(input("Can you guess the number I am thinking? It's less than 20: "))

while num != guess and attempts <4:
    if guess > num:
        print("Your guess is higher")
    else:
        print("Your guess is lower")
    attempts += 1
    guess = int(input("Guess again: "))

if attempts >= 4:
    print("You lost")
else:
    print("You won!")
