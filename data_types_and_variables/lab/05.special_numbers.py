max_number = int(input())


for current_number in range(1, max_number + 1):

    is_special = False
    digit_sum = 0
    current_number = str(current_number)
    for current_digit in current_number:
        current_digit = int(current_digit)
        digit_sum += current_digit

    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special = True

    print(f"{current_number} -> {is_special}")
