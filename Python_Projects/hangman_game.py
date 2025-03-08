import random
words = ("apple", "orange", "banana", "coconut", "pineapple")

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

word = random.choice(words)
hint = ['_']* len(word)
guessed = set()
wrong_guess = 0


def display_hangman(wrong_guess):
    print("******")
    for line in hangman_art[wrong_guess]:
        print(line)
    print("******")

def display_hint(hint):
    print(''.join(hint))


while wrong_guess < len(hangman_art)-1:
    display_hangman(wrong_guess)
    display_hint(hint)

    guess=input("Guess a char: ").lower()
    if not guess.isalpha() or len(guess)!=1:
        print("Please enter only character, Try again!")
        continue

    if guess in guessed:
        print("Character already guessed, Try again!")
        continue

    guessed.add(guess)

    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                hint[i]=guess
    else:
        wrong_guess +=1

    if '_' not in hint:
        display_hangman(wrong_guess)
        print(f"{word} is the word")
        print("You won!")
        break

if '_' in hint:
    display_hangman(wrong_guess)
    print(f"{word} is the word")
    print("you lose!")




