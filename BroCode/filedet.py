# python file detection
# relative file path = folder/test.txt
# Absolute : C:/Users/.....

# import os
#
# file_path = "E:\PythonCourse\BroCode\\test"
# #file_path = "E:\PythonCourse\BroCode"
#
# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists")
#
#     if os.path.isdir(file_path):
#         print("This is a dir")
#     if os.path.isfile(file_path):
#         print("This is a file")
# else:
#     print("Location doesn't exist")

# Python Writing files (.txt, .json,  .csv)
# w-write, r-read, a-append, x-write if file doesn't exist returns error if f exist
# with st. closes the file automatically
# open func returns a file object, access it by aliasing it with as f / file

import json
import csv
data = "I love Python programming!"

# to write a list to file iterate it
fruits = ["Apple", "Banana", "Orange", "Kiwi"]

# json data
employee = {
    "name": "Mano",
    "age": 39,
    "job": "Developer"
}

# csv. list of list - 2d
emp = [["Name", "Age", "Job"],
       ["Jai", "40", "Manager"],
       ["Subhi", "20", "Business"],
       ["Name", "18", "Scientist"]]

try:
    with open("E:\PythonCourse\BroCode\\output", 'x') as f:
        f.write(data)
except FileExistsError as e:
    print(e)
    print("File already exist")

with open("E:\PythonCourse\BroCode\\test", 'w') as f:
    f.write(data)
try:
    with open("E:\PythonCourse\BroCode\\test") as f:
        print(f.read())
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("No Permission to read a file")

with open("E:\PythonCourse\BroCode\\test", 'a') as f:
    f.write("\n" + "I am appending a text")

with open("E:\PythonCourse\BroCode\\test") as f:
    print(f.read())

with open("E:\PythonCourse\BroCode\\test", 'w') as f:
    for item in fruits:
        f.write(item + " ")

# To write and read Json
with open("E:\PythonCourse\BroCode\\output.json", 'w') as f:
    json.dump(employee, f, indent=4)  # converts dict to json
    # dict, fileobj,indentation

with open("E:\PythonCourse\BroCode\\output.json", 'r') as f:
    content = json.load(f)
    print(content)
    # to access a value with key
    print(content["name"])


# To write and read Json
with open("E:\PythonCourse\BroCode\\csval.csv", 'w', newline="") as f: # to avoid newline
    writer = csv.writer(f)
    for row in emp:
        writer.writerow(row)

with open("E:\PythonCourse\BroCode\\csval.csv", 'r') as f: # to avoid newline
    content = csv.reader(f)
    for line in content:
        print(line)
        print(line[2]) # index for specific value

