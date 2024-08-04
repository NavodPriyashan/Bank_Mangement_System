balance = 0  # Global variable for balance

def show_Balance():
    print("****************************")
    print(f"Your Balance is Rs.{balance:.2f}")
    print("****************************")

def deposit():

    global balance
    try:
        print("****************************")
        amount = float(input("Enter an amount to be deposited: "))
        print("****************************")
        if amount < 0:
            print("****************************")
            print("That's not a valid amount")
            print("****************************")
        else:
            balance += amount
    except ValueError:
        print("****************************")
        print("Invalid input. Please enter a number.")
        print("****************************")


def withdraw():

    global balance
    try:
        print("****************************")
        amount = float(input("Enter amount to be Withdraw: "))
        print("****************************")

        if amount > balance:
            print("****************************")
            print("Insufficient Funds")
            print("****************************")
        elif amount < 0:
            print("****************************")
            print("Amount must be greater than 0")
            print("****************************")
        else:
            balance -= amount
    except ValueError:
        print("****************************")
        print("Invalid input. Please enter a number.")
        print("****************************")


def main():
    is_running = True

    while is_running:
        print("****************************")
        print("      Banking Program       ")
        print("****************************")

        print("01. Show Balance")
        print("02. Deposit")
        print("03. Withdraw")
        print("04. Exit")
        print("****************************")


        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_Balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            is_running = False
        else:
            print("****************************")
            print("This is not a valid choice")
            print("****************************")

        print("****************************")
        print("Thank you! Have a nice day!")
        print("****************************")


if __name__ == "__main__":
    main()
