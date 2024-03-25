strings = input().split()
output = ""
for string in strings:
    output += string * len(string)

print(output)
