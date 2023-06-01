import os

def start_list():
    name = input("Enter your name: ")
    filename = name.lower() + ".txt"
    with open(filename, "w") as f:
        while True:
            item = input("Enter an item (or 'x' to stop): ")
            if item == 'x':
                break
            f.write(item + "\n")
    print("List created.")

def add_to_list():
    name = input("Enter your name: ")
    filename = name.lower() + ".txt"
    if not os.path.exists(filename):
        print("List not found.")
        return
    with open(filename, "r") as f:
        items = f.readlines()
        print("Current list:")
        for item in items:
            print(item.strip())
    with open(filename, "a") as f:
        while True:
            item = input("Enter an item to add (or 'x' to stop): ")
            if item == 'x':
                break
            f.write(item + "\n")
    print("Items added to list .")

def print_list():
    name = input("Enter your name: ")
    filename = name.lower() + ".txt"
    if not os.path.exists(filename):
        print("List not found.")
        return
    with open(filename, "r") as f:
        items = f.readlines()
        print("Items:")
        for item in items:
            print(item.strip())

while True:
    print("Main menu:")
    print("1. Start a list")
    print("2. Add to your list")
    print("3. Print your list")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        start_list()
    elif choice == '2':
        add_to_list()
    elif choice == '3':
        print_list()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")