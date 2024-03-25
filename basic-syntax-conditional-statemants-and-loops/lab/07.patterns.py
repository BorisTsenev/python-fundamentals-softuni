pattern_count = int(input())
special_character = "*"
current_row = ""

for first_rows in range(pattern_count):
    for i in range(first_rows + 1):
        current_row += special_character
    print(current_row)
    current_row = ""

for second_rows in range(pattern_count - 1, -1, -1):
    for i in range(second_rows):
        current_row += special_character
    print(current_row)
    current_row = ""

