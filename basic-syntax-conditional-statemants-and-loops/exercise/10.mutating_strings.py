starting_string = input()
target_string = input()


for i in range(1, len(starting_string)): # same length as target_string
    if starting_string[:i] != target_string[:i]:
        left_side = target_string[:i]
        right_side = starting_string[i:]
        starting_string = left_side + right_side
        print(starting_string)

if starting_string[-1] != target_string[-1]:
    print(target_string)
