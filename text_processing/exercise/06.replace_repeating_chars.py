repeating_chars = input()
no_repeating_chars = repeating_chars[0]
for ch in repeating_chars:
    if ch != no_repeating_chars[-1]:
        no_repeating_chars += ch

print(no_repeating_chars)
