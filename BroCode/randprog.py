import random

# print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# number = random.randint(low,high)
# number = random.randint(1,6) # random # from 1 to 6
# number = random.random() # for random floating point numbers
# number = random.choice(options)
random.shuffle(cards)
# print(number)
print(cards)
