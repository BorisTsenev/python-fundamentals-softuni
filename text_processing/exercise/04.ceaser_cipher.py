text = input()
cipher = ""
for ch in text:
    cipher += chr(ord(ch) + 3)
print(cipher)
