places = "=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i="
destinations = []
equal_count = 0
dash_count = 0
current_word = ""
for ch in places:
    if ch == "=":
        equal_count += 1
    elif ch == "/":
        dash_count += 1
    else:
        current_word += ch

    if equal_count == 2:

