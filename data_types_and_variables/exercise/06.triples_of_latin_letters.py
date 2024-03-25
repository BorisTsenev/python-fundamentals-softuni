letters_count = int(input())

for first_char_code in range(97, 97 + letters_count):
    for second_char_code in range(97, 97 + letters_count):
        for third_char_code in range(97, 97+ letters_count):
            output = chr(first_char_code) + chr(second_char_code) + chr(third_char_code)
            print(output)
