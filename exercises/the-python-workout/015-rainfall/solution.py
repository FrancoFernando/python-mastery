"""Exercise 15: Rainfall"""

def print_report(data):
    for city,rain in data.items():
        print(f"{city}: {rain}")

def get_rainfall():
    rainfall = {}
    while True:

        city = input("Enter the name of a city:")

        if not city:
            break

        rain = input("Amount of rain:")
        rainfall[city] = rain
    print_report(rainfall)

get_rainfall()
