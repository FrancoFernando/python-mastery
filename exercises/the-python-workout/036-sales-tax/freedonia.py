"""Exercise 36: Sales Tax"""

tax_percentage = {"Chico": 0.5,
                  "Groucho": 0.7,
                  "Harpo": 0.5,
                  "Zeppo": 0.4}

def calculate_tax(amount, province, hour):
    return amount + (amount * tax_percentage[province] * (hour / 24)) 