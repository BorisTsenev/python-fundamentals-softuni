word = input()
count = 0
index_list = []

for letter in word:
    if letter.isupper():
        index_list.append(count)

    count += 1

print(index_list)
