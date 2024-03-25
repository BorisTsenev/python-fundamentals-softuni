string_count = int(input())

for string in range(string_count):
    current_string = input()
    is_pure = True
    for i in range(len(current_string) - 1):
        if current_string[i] == "," or current_string[i] == "." or current_string[i] == "_":
            is_pure = False

    if is_pure:
        print(f"{current_string} is pure.")
    else:
        print(f"{current_string} is not pure!")
