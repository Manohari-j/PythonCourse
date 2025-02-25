#interpreter - line by line sent to interpreter for execution
#C,C++ - reads full file changes to another file and then send to processor

#Python is dynamically typed lang as we dont use types for var
#print("Hello World") #comment- string-set of characters
#guido van russom
#print - in built function to print

#variables
# name = "Mano" #to store use variable
# print("Hi " + name)
# name = "Jai"
# print("Hi " + name)

#number, floating point,boolean
price=100
amount = 50.3
child = True

#single line comment

'''
Multi line comment
valid: name first_name name_123 _name
invalid - name# name$(only underscore allowed) 1name print(function) abc(not meaningfull)
'''

# Multiple assignment
# name, age, height = "Mano", 39, 169
# print(age)
# like = dislike = 100  # instead of like= 100 dislike= 100
# print(like)


# print factors of n
# 1,2,3,4,6,12 --- 12 ->even- last before is half of its
# 1,3,7,21 --- 21 -> odd less than its half
# 1,2,4,5,10,20,25,50,100-- 100
# so 1 to n/2 but its again linear
# every factor comes with a pair
# num = int(input("Enter a number: "))
# factors = []
# for i in range(1 ,int(num**0.5)+1):
#     if num % i == 0:
#         factors.append(i) #1,2,3
#         if i != num//i:
#             factors.append(num//i)#12,6,4
# factors.sort()
# factors.reverse()
# print(factors)


# to do lists

# tasks = []
# while True:
#     task = input("Enter your to do tasks (enter 'done' to finish): ")
#     if task.lower() == 'done':
#         break
#     tasks.append(task)
#
# print(tasks)

# Peak Element


# for i in range(0, len(arr)):
#
#     if i == 0 and arr[i] > arr[i+1]:
#         peak.append(arr[i])
#
#     elif i == len(arr)-1 and arr[i-1] < arr[i]:
#         peak.append(arr[i])
#
#
#     elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
#         print("I am in mid")
#         peak.append(arr[i])
#
# print(peak)

nums = [3, 20,60,4,70,1, 0]

n=len(nums)
l, r = 0, len(nums) - 1
if len(nums) == 0:
    peak = nums[0]

while l < r:
    mid = (l + r) // 2 # 4 1
    if nums[mid] > nums[mid + 1]: #4>70 1>0
        r = mid # r=1
    else:
        l = mid + 1 # l=70
peak = nums[l]

print(peak)

# move all -ve numbers to the end of the list

l=[3,4,5,-2,-1,2,8,0,-4]

pos =[]
neg= []

for i in range(0,len(l)):
    if l[i]<0:
        neg.append(l[i])
    elif l[i] >= 0:
        pos.append(l[i])

print(pos+neg)


# to run in cmd python file.py
# to compile in cmd python -m py_compile file.py :
# It will create a py cache file and inside it will have exe file

# src file -> RAM - Python Interpreter compiler -> Byte code -> Python Interpreter PVM -> Processor
# src file -> Compiler -> object file -> loaded to RAM -> Processor
# Interpreter step by step interprets. Slow but platform Independent. Use exe/byte code in any OS

# 1. Web Development : Django (complex website building), flask (simple, lightweight websites) - both are frameworks
# 2. Web Scraping: (Automating the task of copying from web instead of manual copying into Excel...)
# It pulls all the data and saves it in required format - BeautifulSoup - it's a module and has many methods
# 3. Web Automation: Selenium - its a python module - controls the browser and fills data for us
# - useful for automation testing
# 4. Data Science: Numpy, Pandas, Matplotlib, OpenCV - libraries used for data analysis
# Numpy - list but faster as it is implemented using C lang - can easily handle multidimensional arrays, math
# Pandas - different type of data are stored in every column of Excel, can easily analyse all data
# Matplotlib - Data visualisation - to present the analysed data from Numpy and pandas
# OpenCV - Image and video processing module - to identify/add any particular obj in an image - face recognition
# 5. GUI - Kivy (Cross platform app), Pyqt5 (Desktop app), Tkinter (old module to build desktop app - beginner version)
# - to build application other than in console (beginner)
# 6. Machine Learning/AI - TensorFlow, PyTorch
# 7. Game - Pygame -Turtle gaming module

# Tech with Tim, Clever Programmer, freeCodeCamp.org
