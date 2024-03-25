def perfect_number(number):
    number_divisors = list()

    for current_number in range(number - 1, 0, -1):
        if number % current_number == 0:
            number_divisors.append(current_number)

    if sum(number_divisors) == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

print(perfect_number(number))
