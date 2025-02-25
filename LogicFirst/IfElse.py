pwd_correct = True
#  alignment is important
if pwd_correct:  # conditional statement
    print("Logged in")
    print("Have a Nice day")
else:
    print("Incorrect Pwd")
    print("try again")

print("bye")

num=30

if num%10 == 0:
    print(str(num)+" is a multiple of 10")
else:
    print(str(num)+" is not a multiple of 10")

# elif ladder
ind_score=360

if ind_score >= 350:
    print("India will win")
elif ind_score >= 250:
    print("India might win")
elif ind_score >= 150:
    print("Aus might win")
else:
    print("Aus will win")

# nested if
# check if the num is 3 digit even number
num = int(input("Enter a num: "))
# if num > 99 and num <1000:
if 99 < num < 1000 and num%2==0:
    if num % 2 == 0:
        print(str(num) + " is a 3 digit even number")
    else:
        print(str(num) + " is a 3 digit odd number")
else:
    print(str(num) + " is not a 3 digit even number")

name = "Mano"

if name[0] == 'M' or name[0] == 'm':
    print("The name starts with M")


