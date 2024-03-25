def add_people(people, wagons: list):
    wagons[len(wagons) - 1] += int(people)
    return wagons


def leave_people(index, people, wagons: list):
    wagons[int(index)] -= int(people)
    return wagons


def insert_people(index, people, wagons: list):
    wagons[int(index)] += int(people)
    return wagons


wagons_count = int(input())
wagons_list = wagons_count * [0]
command = input()

while command != "End":
    command = command.split()

    if command[0] == "add":
        command = add_people(command[1], wagons_list)
    elif command[0] == "insert":
        command = insert_people(command[1], command[2], wagons_list)
    else:
        command = leave_people(command[1], command[2], wagons_list)

    command = input()

print(wagons_list)
