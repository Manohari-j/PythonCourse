# list made of lists, tuples, set

fruits = ["apple", "banana", "orange", "strawberry"]
vegetables = ["carrot", "potato", "beans"]
spices = ["cloves", "cinnamon", "cardamom"]

groceries = [fruits, vegetables, spices]
print(groceries)
print(groceries[0])
print(groceries[1][2])

for items in groceries:
    for x in items:
        print(x, end=" ")
    print()