countries = input().split(", ")
capitals = input().split(", ")

capitals_of_countries = dict(zip(countries, capitals))

for (country, capital) in capitals_of_countries.items():
    print(f"{country} -> {capital}")
