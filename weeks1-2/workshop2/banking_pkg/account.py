def show_balance(balance):
    print("Current balance: ", balance)


def deposit(balance):
    amount = float(input("Enter the amount to deposit:"))
    return balance + amount


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insuficient Funds")
        return balance
    else:
        return print("Current Balance", balance - amount)


def logout(name):
    print("Goodbye", name)
