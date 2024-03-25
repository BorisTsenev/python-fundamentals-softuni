char_sum = 0
first, second = input().split()

for i in range(max(len(first), len(second))):
    current_sum = 0
    if i <= len(first) - 1:
        current_sum += ord(first[i])

    if i <= len(second) - 1:
        if current_sum != 0:
            current_sum *= ord(second[i])
        else:
            current_sum += ord(second[i])

    char_sum += current_sum

print(char_sum)
