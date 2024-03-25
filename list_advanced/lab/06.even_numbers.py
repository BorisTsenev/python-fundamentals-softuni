numbers = list(map(int, input().split(", ")))
indexes_of_even = map(lambda x: x if numbers[x] % 2 == 0 else '', range(len(numbers)))
list_of_indexes = list(filter(lambda a: a != '', indexes_of_even))
print(list_of_indexes)
