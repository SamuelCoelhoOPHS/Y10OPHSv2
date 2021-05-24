food = []
food.append(input("Enter food1 >>>"))
food.append(input("Enter food2 >>>"))
food.append(input("Enter food3 >>>"))
food.append(input("Enter food4 >>>"))

print(food)

item = int(input("Enter number of item to delete>>> "))
item = item-1

del food[item]
print(food)
