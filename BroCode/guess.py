import random

low = 1
high = 100

ans = random.randint(low,high)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {low} and {high}")

while is_running:
    guess = input("Enter a number: ")

    if guess.isdigit():
        guesses +=1
        guess = int(guess)

        if guess<low or guess>high:
            print(f"Please select a number between {low} and {high}")
        elif ans==guess and guesses < 6:
            print("You won!!")
            is_running = False
        elif ans<guess and guesses < 6:
            print("Your guess is higher")
        elif ans>guess and guesses < 6:
            print("Your guess is lower")
        elif guesses >=6:
            print("Better luck next time!!")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {low} and {high}")