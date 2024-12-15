def breakdown_filipino_denomination(amount):
    libo = amount // 1000
    libo_sukli = amount % 1000

    five_h = libo_sukli // 500
    five_sukli = libo_sukli % 500

    two_h = five_sukli // 200
    two_sukli = five_sukli % 200

    one_h = two_sukli // 100
    one_sukli = two_sukli % 100

    fifthy = one_sukli // 50
    fifthy_sukli = one_sukli % 50

    twenty = fifthy_sukli // 20
    twenty_sukli = fifthy_sukli % 20

    ten = twenty_sukli // 10
    ten_sukli = twenty_sukli % 10

    five = ten_sukli // 5
    five_sukli = ten_sukli % 5

    one = five_sukli // 1

    return {
        1000: libo,
        500: five_h,
        200: two_h,
        100: one_h,
        50: fifthy,
        20: twenty,
        10: ten,
        5: five,
        1: one, }

def create_account(accounts, name, initial_deposit):
    accounts[name] = {"balance": initial_deposit}
    print(f"Account created for {name} with balance ₱{initial_deposit}")

def deposit(accounts, name, amount):
    accounts[name]["balance"] += amount
    print(f"\nDeposited: ₱{amount}")
    print(f"New Balance: ₱{accounts[name]['balance']}")

def withdraw(accounts, name, amount):
    if amount > accounts[name]["balance"]:
        print("\nInsufficient funds.")
    else:
        accounts[name]["balance"] -= amount
        print(f"\nWithdrew: ₱{amount}")
        print(f"New Balance: ₱{accounts[name]['balance']}")

def display_balance(accounts, name):
    balance = accounts[name]["balance"]
    print(f"\nCurrent Balance: ₱{balance}")
    print("Denomination Breakdown:")
    breakdown = breakdown_filipino_denomination(balance)
    for denom, count in breakdown.items():
        print(f"₱{denom}: {count}")

def main():
    accounts = {}
    while True:
        print("\nAccount Banking System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance and Denomination Breakdown")
        print("5. Terminate Program")
        ask = input("Choose a Program: ")

        if ask == "1":
            name = input("Enter your name: ")
            initial_deposit = eval(input("Enter initial deposit: "))
            if name in accounts:
                print("Account already exists.")
            else:
                create_account(accounts, name, initial_deposit)

        elif ask == "2":
            name = input("Enter your name: ")
            if name in accounts:
                amount = eval(input("Enter deposit amount: "))
                deposit(accounts, name, amount)
            else:
                print("Account not found.")

        elif ask == "3":
            name = input("Enter your name: ")
            if name in accounts:
                amount = eval(input("Enter withdrawal amount: "))
                withdraw(accounts, name, amount)
            else:
                print("Account not found.")

        elif ask == "4":
            name = input("Enter your name: ")
            if name in accounts:
                display_balance(accounts, name)
            else:
                print("Account not found.")

        elif ask == "5":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
