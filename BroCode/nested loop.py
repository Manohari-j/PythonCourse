# for x in range(1,4): # or for x in range(3)
#     for y in range(1,11):
#         print(y,end="")  # to print the number in same line!!
#     print()

rows = int(input(" Enter the # of rows: "))
cols = int(input(" Enter the # of cols: "))
symbol = input(" Enter a symbol to use: ")
for row in range(rows):
    for col in range(cols):
        print(symbol, end="")
    print()
