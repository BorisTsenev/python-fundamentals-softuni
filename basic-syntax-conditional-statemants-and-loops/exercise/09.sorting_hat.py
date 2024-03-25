command = input()

while True:
    if command == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if command == "Voldemort":
        print("You must not speak of that name!")
        break

    output = ""
    if len(command) < 5:
        output = f"{command} goes to Gryffindor."
    elif len(command) == 5:
        output = f"{command} goes to Slytherin."
    elif len(command) == 6:
        output = f"{command} goes to Ravenclaw."
    else:
        output = f"{command} goes to Hufflepuff."

    print(output)
    command = input()





