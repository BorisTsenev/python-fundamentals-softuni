lines_count = int(input())
opening_brackets = 0
closing_brackets = 0
is_balanced = True

for line in range(lines_count):
    current_line = input()

    if current_line == '(':
        opening_brackets += 1

    if current_line == ')' and opening_brackets == 0:
        print("UNBALANCED")
        is_balanced = False

    if current_line == ')' and opening_brackets == 1:
        opening_brackets = 0

if opening_brackets == 0 and is_balanced:
    print("BALANCED")
