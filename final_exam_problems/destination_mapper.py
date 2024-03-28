places = "/sofia/=varna=/starazagora=/shumen/"
destinations = []
equal_count = 0
dash_count = 0
current_word = ""
for ch in places:
    if ch == "=":
        equal_count += 1
    elif ch == "/":
        dash_count += 1
    current_word += ch

    if equal_count == 2:
        equal_count = 0
        current_word = current_word.replace("=", "")
        if current_word.isalpha():
            destinations.append(current_word)
        current_word = ""
    if dash_count == 2:
        dash_count = 0
        current_word = current_word.replace("/", "")
        if current_word.isalpha():
            destinations.append(current_word)
        current_word = ""

travel_points = 0
for destination in destinations:
    travel_points += len(destination)

print(f"Destinations: {', '.join(destinations)}\nTravel Points: {travel_points}")
