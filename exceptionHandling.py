
try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))

    res = num / den
   # print(res) # give it in else block
except ZeroDivisionError as e: # e has exact error message
    print(e)
    print("cannot divide by zero")
except ValueError as e:
    print(e)
    print("Enter numbers only")
except Exception:  # common/general error. should be given at last only
    print("Error occurred")
else:
    print(res)
finally: # if error is there or not execute this like closing file
    print("This always execute")


print("Last line: bye")
