"""Exercise 15: Rainfall"""

def print_rainfall_report(rainfall_data):
    for city,rain in rainfall_data.items():
        print(f"{city}: {rain}")

def get_rainfall():
    rainfall = {}
    print("Enter rainfall data (press Enter on city name to finish)\n")
    while True:

        city = input("City name:").strip()

        if not city:
            break

        rain = input(f"Rainfall in {city} (mm):")
        rainfall[city] = rainfall.get(city, 0) + int(rain)
    print_rainfall_report(rainfall)

get_rainfall()
