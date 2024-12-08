# Mission 1: Clearing the Field
def clean_city_list(cities):
    return sorted(set(cities))

# Mission 2: High Alert Identification
def analyze_aid_cities(cleaned_cities, previous_intel):
    all_cities = cleaned_cities | previous_intel
    unique_cities = cleaned_cities ^ previous_intel
    high_alert_cities = cleaned_cities & previous_intel
    return all_cities, unique_cities, high_alert_cities

# Mission 3: Detailed City Intel
def get_high_alert_city_data(high_alert_cities, city_data):
    city_info = {city: data for data in city_data for city in high_alert_cities if data[0] == city}
    total_population = sum(data[1] for data in city_info.values())
    total_aid_requests = sum(data[2] for data in city_info.values())
    return city_info, total_population, total_aid_requests

# Mission 4: Tracking Supply Distribution
def track_supply_distribution(supplies):
    supply_distribution = {}
    for city, supply_type, quantity in supplies:
        if city not in supply_distribution:
            supply_distribution[city] = {}
        supply_distribution[city][supply_type] = quantity
    return supply_distribution

#Use Case
# Mission 1
cities = ["Kyiv", "Kharkiv", "Odessa", "Kyiv", "Lviv", "Kharkiv", "Dnipro"]
cleaned_cities = clean_city_list(cities)
print("Cleaned Cities:", cleaned_cities)

# Mission 2
cleaned_cities_set = set(cleaned_cities)
previous_intel = {"Kyiv", "Mariupol", "Lviv", "Donetsk"}
all_cities, unique_cities, high_alert_cities = analyze_aid_cities(cleaned_cities_set, previous_intel)
print("All Cities:", all_cities)
print("Unique Cities:", unique_cities)
print("High-Alert Cities:", high_alert_cities)

# Mission 3
city_data = [
    ("Kyiv", 2800000, 250),
    ("Kharkiv", 1431000, 180),
    ("Lviv", 721301, 90),
    ("Odessa", 1029049, 120),
]
city_info, total_population, total_aid_requests = get_high_alert_city_data(high_alert_cities, city_data)
print("High Alert City Info:", city_info)
print("Total Population:", total_population)
print("Total Aid Requests:", total_aid_requests)

# Mission 4
supplies = [
    ("Kyiv", "Food", 500),
    ("Moscow", "Medicines", 200),
    ("Lviv", "Water", 300),
    ("Saint Petersburg", "Blankets", 100),
    ("Kharkiv", "Food", 150),
]
supply_distribution = track_supply_distribution(supplies)
print("Supply Distribution:", supply_distribution)
