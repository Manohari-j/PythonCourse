# import math
#
# n = int(input("Enter a number: "))
# prime = []
#
# def isPrime(n):
#     for i in range(2, int(math.sqrt(n))+ 1):
#         if n % i == 0:
#             return False
#     return True
#
# for i in range(2,n+1):
#     if isPrime(i):
#         prime.append(i)
#
#
# print(prime)

# Sort a list

# l=[5,2,9,4,1]
# n=len(l)
# for i in range(0,n):
#     for j in range(0,n-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1] = l[j+1],l[j]
#
# print(l)
#
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# if len(A[0]) != len(B):
#         print("Cannot multiply matrices. Incompatible dimensions.")
# res = [[0 for x in range(len(B[0]))] for y in range(len(A))]
# for i in range(len(A)):
#     for j in range(len(B[0])):
#         for k in range(len(B)):
#             res[i][j]=A[i][k]+B[k][j]
#
# print(res)

with open("E:\PythonCourse\FileAssign.txt",'w') as f:
    f.write("Cow moo moo moo \n")

with open("E:\PythonCourse\FileAssign.txt") as f:
    data=f.read()

replacements = {
    'Cow' : 'Duck',
    'moo' : 'quack'
}

for old,new in replacements.items():
    data=data.replace(old,new)
# with open("E:\PythonCourse\FileAssign.txt",'r+') as f:
#     data = data.replace("Cow", "Duck")

with open("E:\PythonCourse\FileAssign.txt",'a') as f:
    f.write(data)
with open("E:\PythonCourse\FileAssign.txt") as f:
        print(f.read())



