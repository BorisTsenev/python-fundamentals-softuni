def add_and_subtract(a, b, c):
    def sum_numbers(num1, num2):
        sum_of_numbers = num1 + num2
        return sum_of_numbers

    sum_of_first_two = sum_numbers(a, b)

    def subtract(num1, num2):
        subtracted = num1 - num2
        return subtracted

    return subtract(sum_of_first_two, c)


first_number = int(input())
second_number = int(input())
third_number = int(input())

output = add_and_subtract(first_number, second_number, third_number)

print(output)
