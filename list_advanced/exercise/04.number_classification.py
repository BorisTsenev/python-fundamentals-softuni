def number_classification(numbers_sequence):
    numbers = list(map(int, numbers_sequence.split(", ")))
    positive_nums = [str(number) for number in numbers if number >= 0]
    negative_nums = [str(number) for number in numbers if number < 0]
    even_nums = [str(number) for number in numbers if number % 2 == 0]
    odd_nums = [str(number) for number in numbers if number % 2 != 0]

    return f"Positive: {', '.join(positive_nums)} \n" \
           f"Negative: {', '.join(negative_nums)} \n" \
           f"Even: {', '.join(even_nums)} \n" \
           f"Odd: {', '.join(odd_nums)}"


numbers = input()
print(number_classification(numbers))
