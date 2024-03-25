chars = input().split(", ")
chars_with_values = {}

for char in chars:
    chars_with_values[char] = ord(char)

print(chars_with_values)
