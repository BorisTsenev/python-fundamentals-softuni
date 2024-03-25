gifts = input().split()

command = input()

while command != "No Money":
    command = command.split()
    if command[0] == "OutOfStock":
        while True:
            if command[1] in gifts:
                gifts[gifts.index(command[1])] = "None"
            else:
                break
    elif command[0] == "Required":
        current_gift = command[1]
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = current_gift
    elif command[0] == "JustInCase":
        gifts[-1] = command[1]
    command = input()

while True:
    if "None" in gifts:
        gifts.remove("None")
    else:
        break

print(' '.join(gifts))
