def absolute_list(list_of_nums):
    abs_list = list()
    for number in list_of_nums:
        abs_list.append(abs(number))

    return abs_list


random_list = map(float, input().split())
new_list = absolute_list(random_list)
print(new_list)
