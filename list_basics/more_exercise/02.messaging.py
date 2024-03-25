message_indexes = input().split()
string_input = input()
list_of_string = list(string_input)
message = ""

for current_message in range(len(message_indexes)):
    digit_sum = 0
    for digit in message_indexes[current_message]:
        digit_sum += int(digit)

    digit_index = digit_sum % (len(string_input))
    message += list_of_string.pop(digit_index)

print(message)
