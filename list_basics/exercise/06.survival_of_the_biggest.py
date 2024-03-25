input_numbers = input()
input_list = [int(x) for x in input_numbers.split()]

max_numbers_count = int(input())

for _ in range(max_numbers_count):
    input_list.remove(min(input_list))

output = ', '.join(map(str, input_list))
print(output)
