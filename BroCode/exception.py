# An event that interrupts the flow of a program
# ZeroDivisionError - 1/0, TypeError - 1+"1", ValueError: typecasting wrong value - int("Pizza")
# try, except, finally

try:
    num = int(input("Enter a number: "))
    print(1/num)

except ZeroDivisionError as e:
    print(e)
    print("You can't divide a number by 0")

except ValueError as e:
    print(e)
    print("Enter only numbers")

except Exception:
    print("Error")

finally: # cleanup like closing a file...
    print("Good bye!")


