input_digits = input()
digits_list = []
max_num = ""

for digit in input_digits:
    digits_list.append(digit)

for digit in range(len(digits_list)):
    max_digit = str(max(digits_list))
    max_num += max_digit
    digits_list.remove(max(digits_list))

print(max_num)

