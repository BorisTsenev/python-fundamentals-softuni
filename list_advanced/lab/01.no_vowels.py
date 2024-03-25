text_input = input()
forbidden_chars_lower = ['a', 'o', 'u', 'e', 'i']
forbidden_chars_upper = [up_let.upper() for up_let in forbidden_chars_lower]
forbidden_chars = forbidden_chars_upper + forbidden_chars_lower

output = [letter for letter in text_input if letter not in forbidden_chars]
print(''.join(output))
