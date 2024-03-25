list_length = int(input())
special_word = input()
list_of_strings = []

for line in range(list_length):
    current_line = input()
    list_of_strings.append(current_line)

filtered_list_of_strings = list_of_strings.copy()

for element in filtered_list_of_strings:
    if special_word not in element:
        filtered_list_of_strings.remove(element)

print(list_of_strings)
print(filtered_list_of_strings)
