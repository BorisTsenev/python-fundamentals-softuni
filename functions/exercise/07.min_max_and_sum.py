def min_max_and_sum(numbers_in_string):
    list_of_nums = list(map(int, numbers_in_string.split()))

    min_num = min(list_of_nums)
    max_num = max(list_of_nums)
    sum_of_nums = sum(list_of_nums)

    return f"The minimum number is {min_num}\n" \
           f"The maximum number is {max_num}\n" \
           f"The sum number is: {sum_of_nums}"


numbers = input()
print(min_max_and_sum(numbers))
