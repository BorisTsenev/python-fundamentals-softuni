while True:
    command = input()
    if command == "end":
        break

    rev_word = "".join([k for k in reversed(command)])
    print(f"{command} = {rev_word}")
