chars = input()
digits = ""
alpha = ""
other = ""
for char in chars:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        alpha += char
    else:
        other += char

print(f"{digits}\n{alpha}\n{other}")
