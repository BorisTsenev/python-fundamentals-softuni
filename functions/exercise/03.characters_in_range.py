# ord() za ascii
char_output = list()
def characters_in_range(char1, char2):
    start = ord(char1)
    end = ord(char2)

    for ascii_code in range(start + 1, end):
        char_output.append(chr(ascii_code))

    return ' '.join(char_output)


first_char = input()
second_char = input()

print(characters_in_range(first_char, second_char))
