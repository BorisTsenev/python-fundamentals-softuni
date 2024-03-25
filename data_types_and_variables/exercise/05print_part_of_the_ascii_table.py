ascii_start = int(input())
ascii_end = int(input())
output = ""

for char_code in range(ascii_start, ascii_end + 1):
    current_char = chr(char_code)
    output += current_char + " "

print(output)
