# recursion - a function calling itself
# def factorial(n):
#     if n==0:
#         return 1
#     return n*factorial(n-1)
#
#
# print(factorial(5))

# Generators

def sq(num):
    s=[]
    for i in range(1,num+1):
        s.append(i*i)
    return s

print(sq(10))

# generator is useful for large number of values
# in list all will go in memory as a whole, so better to use gen for large no of values
def sq_gen(num):
    for i in range(1,num+1):
        yield i*i # generate and send every number

gen=sq_gen(10) # returns as object
for i in gen:
    print(i)

