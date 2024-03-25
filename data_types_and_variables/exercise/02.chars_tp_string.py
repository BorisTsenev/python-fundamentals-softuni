list_of_chars = list()
for char in range(3):
    list_of_chars.append(input())

list_of_chars = "".join(str(char) for char in list_of_chars)

print(list_of_chars)
