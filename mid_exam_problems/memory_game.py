elements = input().split()
tries = 0

while True:
    command = input()
    if len(elements) == 0:
        print(f"You have won in {tries} turns!")
        break
    if command == "end":
        if len(command) == 0:
            print(f"You have won in {tries} turns!")
        else:
            print(f"Sorry you lose :(\n" + " ".join(elements))
        break

    command = list(map(int, command.split()))
    if command[0] not in range(len(elements)) or command[1] not in range(len(elements)):
        mid_index = int(len(elements) / 2)
        for _ in range(2):
            elements.insert(mid_index, f"-{tries + 1}a")
        print("Invalid input! Adding additional elements to the board")
        tries += 1
        continue

    if elements[command[0]] == elements[command[1]]:
        print(f"Congrats! You have found matching elements - {elements[command[0]]}!")
        item = elements[command[0]]
        elements.remove(item)
        elements.remove(item)

    else:
        print("Try again!")

    tries += 1
