digits_in_string = input().split(", ")
digits = [eval(i) for i in digits_in_string]
zero_count = 0

for digit in range(len(digits)):
    if digits[digit] == 0:
        zero_count += 1

for _ in range(zero_count):
    digits.remove(0)
    digits.append(0)

print(digits)