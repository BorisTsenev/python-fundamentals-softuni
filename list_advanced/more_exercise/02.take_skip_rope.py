hidden_message = input()
numbers = [num for num in hidden_message if num.isdigit()]
take_list = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
skip_list = [numbers[i] for i in range(len(numbers)) if i % 2 == 1]
hidden_message_list = [letter for letter in hidden_message if not letter.isdigit()]

output = list()
for current_rope in range(len(take_list)):
    for take in range(int(take_list[current_rope])):
        if len(hidden_message_list) > 0:
            output.append(hidden_message_list.pop(0))

    for skip in range(int(skip_list[current_rope])):
        if len(hidden_message_list) > 0:
            hidden_message_list.pop(0)

print(''.join(output))
