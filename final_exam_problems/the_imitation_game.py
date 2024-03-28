def move(word, letters_count):
    word = [x for x in word]
    for _ in range(letters_count):
        word.append(word.pop(0))

    return ''.join(word)


def insert(word, index, value):
    word = [x for x in word]
    word.insert(index, value)
    return ''.join(word)


def change_all(word, substring, replacement):
    return word.replace(substring, replacement)


message = input()

while True:
    command = input()
    if command == "Decode":
        print(f"The decrypted message is: {message}")
        break

    command = command.split("|")
    if command[0] == "ChangeAll":
        message = change_all(message, command[1], command[2])
    elif command[0] == "Insert":
        message = insert(message, int(command[1]), command[2])
    elif command[0] == "Move":
        message = move(message, int(command[1]))
