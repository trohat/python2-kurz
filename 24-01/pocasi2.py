rainfall = {}

while True:
    city = input("Zadej město: ")
    if not city:
        break

    actual_rain = int(input("Zadej kolik pršelo "))

    old_value = rainfall.get(city, { "rain": 0, "days": 0})

    rainfall[city] = {
        "rain": actual_rain + old_value["rain"],
        "days": 1 + old_value["days"]
    }

print(rainfall)

for mesto, value in rainfall.items():
    print(f"v {mesto} napršelo průměrně \
{value['rain'] / value['days']} mm deště")