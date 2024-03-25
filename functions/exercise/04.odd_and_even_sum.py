def odd_even_sum(num):
    even_sum = 0
    odd_sum = 0
    list_of_digits = list()

    for current_digit in num:
        if current_digit != 0:
            list_of_digits.append(int(current_digit))

    for digit in list_of_digits:
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
print(odd_even_sum(number))
