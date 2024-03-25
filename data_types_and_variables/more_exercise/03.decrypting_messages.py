key = int(input())
message_length = int(input())
decrypted_message = ""

for chars in range(message_length):
    current_char = input()

    decrypted_char_code = ord(current_char) + key
    decrypted_message += chr(decrypted_char_code)

print(decrypted_message)
