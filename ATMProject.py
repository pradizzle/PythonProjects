import csv

transactions = []

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Log in")
        print("2. Add user")
        print("3. Quit")

        choice = input("Choose your action: ")

        if choice == "1":
            login()
        elif choice == "2":
            add_user()
        elif choice == "3":
            print("Have a good day. Now go make that bread!!")
            break
        else:
            print("Invalid input. Please try again.")

def withdraw(username):
    with open(f"{username}.txt", "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        checking_balance = float(data[1][1])
        savings_balance = float(data[2][1])

        print("Checking balance: " + str(checking_balance))
        print("Savings balance: " + str(savings_balance))

        account = int(input("Which account would you like to withdraw from?"+"\n" +"1: checking"+"\n" +"2: savings"+"\n" +"Enter your account type selection:"))
        while account not in [1,2]:
            print("Invalid account, please try again")
            account = int(input("Which account would you like to withdraw from?"+"\n" +"1: checking"+"\n" +"2: savings"+"\n" +"Enter your account type selection:"))
        
        amount = float(input("How much would you like to withdraw? "))
        while amount <= 0:
            print("Invalid amount, please try again")
            amount = float(input("How much would you like to withdraw? "))

        if account == 1:
            if amount > checking_balance:
                print("Insufficient funds, returning to main menu")
                return
            checking_balance -= amount
            transactions.append(f"{username} withdrew ${amount} from checking")
        else:
            if amount > savings_balance:
                print("Insufficient funds, returning to main menu")
                return
            savings_balance -= amount
            transactions.append(f"{username} withdrew ${amount} from savings")
        data[1][1] = checking_balance
        data[2][1] = savings_balance

        with open(f"{username}.txt", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        
        print("Withdrawal successful")

def deposit(username):
    with open(f"{username}.txt", "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        checking_balance = float(data[1][1])
        savings_balance = float(data[2][1])

        print("Checking balance: " + str(checking_balance))
        print("Savings balance: " + str(savings_balance))

        account = int(input("Which account would you like to deposit to?"+"\n" +"1: checking"+"\n" +"2: savings"+"\n"+"Enter your account type selection:"))
        while account not in [1,2]:
            print("Invalid account, please try again")
            account = int(input("Which account would you like to deposit to?"+"\n" +"1: checking"+"\n" +"2: savings"+"\n"+"Enter your account type selection:"))
        
        amount = float(input("How much would you like to deposit? "))
        while amount <= 0:
            print("Invalid amount, please try again")
            amount = float(input("How much would you like to deposit? "))

        if account == 1:
            checking_balance += amount
            transactions.append(f"{username} deposited ${amount} to checking")
        else:
            savings_balance += amount
            transactions.append(f"{username} deposited ${amount} to savings")

        data[1][1] = checking_balance
        data[2][1] = savings_balance

        with open(f"{username}.txt", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        
        print("Deposit successful")

def print_receipt(username):
    with open(f"{username}.txt", "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        checking_balance = float(data[1][1])
        savings_balance = float(data[2][1])

        print("Checking balance: " + str(checking_balance))
        print("Savings balance: " + str(savings_balance))

        with open(f"{username}_receipt.txt", "w") as receipt:
            receipt.write("Thank you for banking with us "+ username +"!" + "\n")
            receipt.write("Checking balance: " + str(checking_balance)+"\n")
            receipt.write("Savings balance: " + str(savings_balance)+"\n")
            receipt.write("Transactions:" + "\n")
            print("Transactions:")
            for transaction in transactions:
                print(transaction)
                receipt.write(transaction + "\n")

        print("Receipt printed successfully!")

def change_pin(username):
    with open("users.txt", "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        
    for index, row in enumerate(data):
        if row[0] == username:
            new_pin = input("Enter your new PIN: ")
            conf_pin = input("Confirm your new PIN: ")
            while new_pin != conf_pin:
                print("PINs do not match, please try again")
                new_pin = input("Enter your new PIN: ")
                conf_pin = input("Confirm your new PIN: ")
            data[index][1] = new_pin

            print("PIN changed successfully")

            with open("users.txt", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            return

    print("Username not found, returning to main menu")

def user_menu(username):
    while True:
        print("Welcome, " + username + "!")
        print("1. Withdraw money")
        print("2. Deposit money")
        print("3. Print receipt")
        print("4. Change PIN")
        print("5. Log out")

        choice = input("What would you like to do?")

        if choice == "1":
            withdraw(username)
        elif choice == "2":
            print("Deposit")
            deposit(username)
        elif choice == "3":
            print("Print receipt")
            print_receipt(username)
        elif choice == "4":
            print("Change PIN")
            change_pin(username)
        elif choice == "5":
            print("Logging out")
            break
        else:
            print("Invalid input. Please try again.")
            
def login():
    username = input("Enter your username: ")
    with open("users.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                for i in range(3):
                    pin = input("Enter your PIN: ")
                    if row[1] == pin:
                        user_menu(username)
                        return
                    print("Incorrect PIN, please try again")
                print("Too many failed attempts, returning to main menu")
                return
    print("Username not found, returning to main menu")

def add_user():
    user_pin = input("Enter admin PIN: ")
    with open("admin.txt", "r") as file:
        user_data = file.readline().strip().split(",")
        if user_data[1] != user_pin:
            print("Incorrect admin PIN, returning to main menu")
            return

    new_username = input("Enter new username: ")
    new_pin = input("Enter new PIN: ")
    confirm_pin = input("Confirm new PIN: ")
    while new_pin != confirm_pin:
        print("PINs do not match, please try again")
        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")

    with open("users.txt", "a") as file:
        writer = csv.writer(file)
        writer.writerow([new_username, new_pin])

    with open(f"{new_username}.txt", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Account Type", "Balance"])
        writer.writerow(["Checking", 500])
        writer.writerow(["Savings", 1000])

    print("User added successfully")

main_menu()