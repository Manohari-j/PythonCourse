# an object/collection that can return its elements one at a time
# allowing it to be iterated over in a loop
# List[], tuples(), set{}, dictionary:{k:v}, string - characters can be iterated
# Membership operators : in, not in
# List Comprehension: A concise way to create lists in python.
# [exp for value in iterable if condn]

# doubles = []
#
# for x in range(1,11):
#     doubles.append(x*2)
#
# print(doubles)

doubles = [x*2 for x in range(1,11)]
triples = [y*3 for y in range(1,11)]
squares = [z*z for z in range(1,11)]

print(squares)
print(doubles)
print(triples)

fruits = ["apple","orange","banana","coconut"]
fruit_list = [fruit.upper() for fruit in fruits]
print(fruit_list)

numbers = [1,-2,3,-4,5,-6]
pos = [n for n in numbers if n>0]
print(pos)