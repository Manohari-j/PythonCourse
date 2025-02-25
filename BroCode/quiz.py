questions = ("How many elements are there in periodic table?",
             "Which animal lays the largest eggs?",
             "What is the most abundant gas in Earth's atmosphere?",
             "How many bones are in human body?",
             "Which planet in the solar system is the hottest?")
options = (("A. 116 ", "B. 117 ", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
answers = ("C", "D", "A", "A", "B",)
guesses = []
score = 0
ques_num = 0

for q in questions:
    print("----------------------------")
    print(q)
    for option in options[ques_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[ques_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[ques_num]} is the correct answer.")
    ques_num += 1

print("---------------------")
print("       RESULTS      ")
print("---------------------")

print("Answers: ", end="")
for a in answers:
    print(a, end = " ")
print()

print("Guesses: ", end="")
for g in guesses:
    print(g, end = " ")
print()


score = int(score/len(questions) * 100)
print(f"Your score is {score}%")
