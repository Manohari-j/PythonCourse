import math #math - module

a=10
b=5
print(a+b, a-b, a*b, a/b)
# division automatically gives the float output
print(a+b*5 , (a+b)*5)

a=8.78
print(round(a))
a=-5
print(abs(a))
a=5
print(pow(a,3))
print(a**3)#a cube ** power
print(a**2)#a square

a=7
b=8

print(max(a,b))
print(min(a,b))

a=4.56
print(math.ceil(a))
print(math.floor(a))
print(math.factorial(b))

num = int(input("Enter a value"))
print(math.log(num,2))
print(math.cos(num))
