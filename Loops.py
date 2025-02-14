# loops - repeats a set of code - while, for

# letter = ' '
# while not letter.isalpha():
#     letter = input("Enter an alphabet: ")
#
# print("You have entered " + letter)

# print 1 to 100

# i = 1
#
# while i <= 100:
#     print(i)
#     i += 1



# in cmd
#  list(range(1,10))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> list(range(20,31,2))
# [20, 22, 24, 26, 28, 30]
# >>> list(range(10,0,-1))
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# last number is not included
# else in For loop to execute false statement
# for i in range(1,101):
#     print(i)
# else:
#     print("end")

# list = [1,3,5,7,9]
#
# for i in list:
#     print(i*i)

# Nested Loops
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=' ')  # to print in the same line
#     print('')

# break,continue,pass
# get list of numbers and add to list

# print("Enter List of numbers (Enter z to exit) ")
# li=[]
# while True:
#     inp = input()
#     if inp == 'z':
#         break
#     li.append(int(inp))
#
# print(li)

# using walrus op
print("Enter List of numbers (Enter z to exit) ")
li=list()
while (inp := input()) != 'z':
    li.append(int(inp))

print(li)

# remove , from a string
str = "A,B,V,C,E,R"
s=''

# for i in str:
#     if i == ',':
#         continue
#     s += i
# print(s)

# pass: placeholder. do nothing. it doesn't go to next loop, it just go to next statement

# for i in str:
#     if i == ',':
#         pass
#     else:
#         s += i
# print(s)


# find a multiple of 20 >= n

# n= int(input("Enter a number: "))
#
# for i in range(n,n+20):
#     if i%20==0:
#         print(i)
#         break

#

# walrus operator := assigns as well as do some extra tasks
# name="Mano"
# print(name)

print(name := "Mano")






