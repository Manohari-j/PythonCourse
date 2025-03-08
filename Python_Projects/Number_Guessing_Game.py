# Build a Number guessing game, in which the user selects a range.
# Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
import math
import random


start_range = int(input("Enter a number for beginning range: "))
end_range = int(input("Enter a number for ending range: "))
num = random.randint(start_range,end_range)

guess_count = 0
allowed_guesses =int(math.log2(end_range-start_range+1))
print(allowed_guesses)
while guess_count < allowed_guesses:
    guess = input(f"Guess a number between {start_range} and {end_range}: ")
    if not guess.isdigit():
        print("Please enter a number, Try again")
        continue
    guess_count += 1

    guess = int(guess)

    if guess == num:
        print("You Won")
        break
    elif guess < num:
        print("Your guess is lower!")
    else:
        print("Your guess is higher!")

print(f"Total number of guesses is {guess_count}")
if guess_count > allowed_guesses:
    print("Your chance is over. You lose!")

print("Thank You!!")


