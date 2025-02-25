# Single variable used to store multiple values
# List = [] Ordered and Changeable. Duplicates ok
# Set = {} unOrdered and Immutable. but add/remove ok, No Duplicates
# Tuple = () Ordered and unChangeable. Duplicates ok. Faster
# dictionary = a collection of {Key:value} pairs. ordered and changeable. No duplicates


# fruits = ["Apple","Orange","Banana","Kiwi"]
# print(fruits)
# print(fruits[0:4:2])
# print(fruits[::-1])
# print(len(fruits))
# print("Apple" in fruits)
# fruits.append("Pineapple")
# fruits . remove("Kiwi")
# fruits.insert(2,"Watermelon")
# # fruits[3] = "Apple"
# # print(dir(fruits))
# # print(help(fruits))
# for x in fruits:
#     print(x)
#
# # fruits.sort()
# # fruits.reverse()
# print(fruits)
# print(fruits.index("Watermelon"))
# print(fruits.count("Apple"))


# fruits = {"Apple","Orange","Banana","Kiwi","Kiwi"}  # it allows duplicates but display only one item of it
# print(fruits)  # not ordered
# # indexing is not possible
# print(len(fruits))
# print("Apple" in fruits)
# fruits.add("Watermelon")
# #fruits.remove("Kiwi")
# #fruits.pop()
# print(fruits)
#
#
# for x in fruits:
#    print(x)
# print(fruits)

# indexing is available in tuple
# fruits = ("Apple","Orange","Banana","Kiwi")
# print(fruits)
# print(fruits[0:4:2])
# print(fruits[::-1])
# print(len(fruits))
# print("Apple" in fruits)

# print(dir(fruits))
# print(help(fruits))
# for x in fruits:
#     print(x)
#
# print(fruits)
# print(fruits.index("Apple"))
# print(fruits.count("Apple"))

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals)
# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA")) # returns value for the given key
print(capitals.get("Japan")) # returns None

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Washington"})
print(capitals)

#capitals.pop("China") # removes given item
capitals.popitem() # removes last item
print(capitals)
print(capitals.keys())
print(capitals.values())

for k in capitals.keys():
    print(k)

for v in capitals.values():
    print(v)

print(capitals.items()) # 2d list of tuples [(),(),()]

for k,v in capitals.items():
    print(f"{k}:{v}")
