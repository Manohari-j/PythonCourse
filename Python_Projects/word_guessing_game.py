# simple word-guessing game where the user has to guess the characters in a
# randomly selected word within a limited number of attempts.

import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
word_length = len(word)
clue = ['_'] * word_length
wrong_guess = 0
allowed_guesses = 6
guess = ''
guessed_letter = set()

while wrong_guess < allowed_guesses:
    print(" ".join(clue))
    guess = input(f"Guess the letter: ")

    if len(guess)!=1 or not guess.isalpha():
        print("Please enter a letter only!")
        continue

    if guess in guessed_letter:
        print("Guessed already, Try again!")
        continue
    else:
        guessed_letter.add(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                clue[i] = guess
    else:
        wrong_guess +=1

    if '_' not in clue:
        break


print("***************************************")
if wrong_guess == allowed_guesses:
    print("Better Luck next time! You Lost!")
else:
    print("You Won!!!")

print("Thank you for playing the game!")
print("***************************************")




