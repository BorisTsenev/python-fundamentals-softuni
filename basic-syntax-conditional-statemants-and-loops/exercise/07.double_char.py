command = input()


while not command == "End":
    output_string = ""
    for i in range(len(command)):
        output_string += command[i] + command[i]

    if command != "SoftUni":
        print(output_string)

    command = input()