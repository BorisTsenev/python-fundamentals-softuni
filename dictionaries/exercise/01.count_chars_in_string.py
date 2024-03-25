text_chars = list(input())
chars = list(dict.fromkeys(text_chars))
counted_chars = {}
for char in chars:
    if char != " ":
        counted_chars[char] = text_chars.count(char)

for (char, count) in counted_chars.items():
    print(f"{char} -> {count}")
