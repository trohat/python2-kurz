menu = {}
menu["fish"] = 5
menu["pizza"] = 10
menu["dessert"] = 15
menu["steak"] = 25
menu["appetizers"] = 5
menu["drinks"] = 5


bill = 0
while True:
    choice = input("choose your dish: ")
    if choice == "finished":
        break
    
    if choice in menu:
        bill = bill + menu[choice]
        print(f"you ordered {choice} for ${menu[choice]}")
        print(f"the bill for your meal is {bill}")
    else:
        print("we're sorry we dont have your order")


print(f"the bill for your meal is {bill}")