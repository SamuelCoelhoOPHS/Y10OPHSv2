print("MarioKart Menus:")
choice = 0

def menu():
    print("1) 1-player")
    print("2) 2-player")
    print("3) Online")
    print("4) Exit")

    choice=int(input("Choose 1,2,3 or 4: >> "))

    if choice ==1:
        print("1 player selected")

    if choice ==2:
        print("2 player selected")

    if choice ==3:
        print("Online mode selected")

    if choice ==4:
        print("Exiting......")
menu()
