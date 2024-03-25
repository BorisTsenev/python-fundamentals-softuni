def group_of_tens(numbers: list):
    groups_count = max(numbers) // 10
    if max(numbers) % 10 != 0:
        groups_count += 1
    output = ""
    for current_multiply in range(1, groups_count + 1):
        current_tens = 10 * current_multiply
        current_nums = [num for num in numbers if current_tens - 10 < num <= current_tens]
        output += f"Group of {current_tens}'s: {current_nums}\n"

    return output


nums_list = list(map(int, input().split(", ")))
print(group_of_tens(nums_list))
