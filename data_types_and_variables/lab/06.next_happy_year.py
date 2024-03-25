current_year = int(input())

while True:
    current_year += 1
    current_year = str(current_year)
    is_happy = True
    previous_digits = ""

    for digit in current_year:
        if digit in previous_digits:
            is_happy = False
            break
        else:
            pass

        previous_digits += digit

    if is_happy:
        print(current_year)
        break

    current_year = int(current_year)