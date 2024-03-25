messages_count = int(input())

for message in range(messages_count):
    message_code = int(input())

    if message_code == 88:
        message = "Hello"
    elif message_code == 86:
        message = "How are you?"
    elif message_code < 88:
        message = "GREAT!"
    else:
        message = "Bye."

    print(message)
