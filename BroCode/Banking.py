def show_balance(balance):
    print("*********************************")
    print(f"Your balance is ${balance:.2f}")
    print("*********************************")


def deposit():
    print("*********************************")
    amount = float(input("Enter an amount to be deposited: "))
    if amount<0:
        print("That is not a valid amount")
        return 0
    else:
        return amount


def withdraw(balance):
    print("*********************************")
    withdrawal_amount = float(input("Enter an amount to be withdrawn: "))
    if withdrawal_amount > balance:
        print("Insufficient funds")
        return 0
    elif withdrawal_amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return withdrawal_amount


def main():
    balance = 1000
    amount = 0
    while True:

        print("*********************************")
        print("        Banking Program          ")
        print("*********************************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*********************************")
        ch = int(input("Enter your choice(1-4): "))

        if ch == 1:
            show_balance(balance)
        elif ch == 2:
            amount = deposit()
            balance += amount
            print("*********************************")
        elif ch == 3:
            withdrawal_amount=withdraw(balance)
            balance -= withdrawal_amount
            print("*********************************")
        elif ch == 4:
            quit()
        else:
            print("Invalid choice")


    print("Thank you, Have a nice day!")


if __name__ == '__main__':
    main()