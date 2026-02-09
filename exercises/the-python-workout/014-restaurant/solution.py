"""Exercise 14: Restaurant"""

MENU = {"margherita":15, "napoli":16, "capricciosa":23, "funght":20, "focaccia":12}

def restaurant():
    total = 0
    while order := input("make an order:"):
        if order in MENU:
            total += MENU[order]
        else:
            print("the dish is not on the menu")
    print(f"The total is: {total}")

restaurant()