phonebook = {}
calls_count = 0

while True:
    command = input()
    if "-" not in command:
        calls_count = int(command)
        break

    name, number = command.split("-")
    phonebook[name] = number

for _ in range(calls_count):
    name = input()
    if name not in phonebook.keys():
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook[name]}")
