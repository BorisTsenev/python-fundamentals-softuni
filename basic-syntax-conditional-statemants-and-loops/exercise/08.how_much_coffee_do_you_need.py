command = input()
coffee_count = 0

while not command == "END":
    if command.isupper():
        if command == "CODING" or command == "CAT" or command == "DOG" or command == "MOVIE":
            coffee_count += 2
    else:
        if command == "coding" or command == "cat" or command == "dog" or command == "movie":
            coffee_count += 1

    command = input()

if coffee_count > 5:
    output = "You need extra sleep"
else:
    output = coffee_count

print(output)
