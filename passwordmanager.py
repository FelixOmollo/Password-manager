pwd = input("Enter the master password ")

def view():
    pass

def add():
    pass

while True:
    mode = input("Do you want to view or add a password?(view/add) To quit type q. ").lower()
    if mode == "q":
        break
    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode")
        continue
