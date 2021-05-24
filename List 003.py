names = []

names.append(input("Enter name1 >>>"))
names.append(input("Enter name2 >>>"))
names.append(input("Enter name3 >>>"))

moreName = True
while moreName == True:
    newName = str(input("Do you want to add another name? >>"))
    if newName == "no":
        print(names)
        moreName = False

    else:
        if newName == "yes":
            names.append(input("Enter name >>>"))
