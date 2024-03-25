def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


list_of_nums = map(int, input().split())
output = list(filter(is_even, list_of_nums))

print(output)
