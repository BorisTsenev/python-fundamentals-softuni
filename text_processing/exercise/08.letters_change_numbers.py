operations = input().split()
total_sum = 0

for current_operation in operations:
    first_letter = current_operation[0]
    last_letter = current_operation[-1]
    number = int(current_operation[1:-1])

    first_letter_position = ord(first_letter.lower()) - 96
    last_letter_position = ord(last_letter.lower()) - 96
    if first_letter.isupper():
        number /= first_letter_position
    else:
        number *= first_letter_position

    if last_letter.isupper():
        number -= last_letter_position
    else:
        number += last_letter_position

    total_sum += number

print(f"{total_sum:.2f}")
