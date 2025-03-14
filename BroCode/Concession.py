menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25
        }

cart = []
total = 0

print("-------MENU--------")
for k, v in menu.items():
    print(f"{k:10}: ${v:.2f}")
print("--------------------")

while True:
    food=input("Select an item(q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item is not available, Please select from the list")

print("------Your Order------")
for food in cart:
    total += menu.get(food)
    print(food,end=" ")
print()
print("-----------------------")
print(f"Your total is ${total:.2f}")
