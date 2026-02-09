"""Exercise 14: Restaurant"""

MENU = {"margherita":15, "napoli":16, "capricciosa":23, "funght":20, "focaccia":12}

def restaurant():
    total = 0
    while order := input("make an order:"):
        if order in MENU:
            price = MENU[order]
            total += price
            print(f"order costs {price}, total is {total}")
        else:
            print("the dish is not on the menu")
    print(f"The total is: {total}")

restaurant()