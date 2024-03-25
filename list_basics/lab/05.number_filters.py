numbers_count = int(input())
list_of_numbers = []

for number in range(numbers_count):
    current_number = int(input())
    list_of_numbers.append(current_number)

command = input()
output_list = []

for number in list_of_numbers:
    is_true = False
    if command == "even" and number % 2 == 0 \
            or command == "odd" and number % 2 == 1 \
            or command == "positive" and number >= 0 \
            or command == "negative" and number < 0:
        is_true = True

    if is_true:
        output_list.append(number)

print(output_list)
