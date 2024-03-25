chars_count = int(input())
chars_sum = 0

for char in range(chars_count):
    current_char = input()
    chars_sum += ord(current_char)

print("The sum equals: " + str(chars_sum))
