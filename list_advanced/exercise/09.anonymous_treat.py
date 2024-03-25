def main():
    input_list = input().split()
    command = input()
    while command != "3:1":
        command = command.split()
        if command[0] == 'merge':
            input_list = merge(input_list, int(command[1]), int(command[2]))
        else:
            pass
        command = input()


def merge(input_list, start_index, end_index):
    if start_index < 0:
        start_index = 0

    if end_index > len(input_list) - 1:
        end_index = len(input_list) - 1

    merged_elements = ""
    for current_merge in range(start_index, end_index):
        merged_elements += input_list[current_merge]
        input_list.pop(current_merge)

    input_list.insert(start_index, merged_elements)

    return input_list


def divide(input_list, index, parts):
   pass


main()
