usernames = input().split(", ")
valid_usernames = []
valid_chars = ["-", "_"]
for username in usernames:

    if 3 <= len(username) <= 16:
        is_valid = True
        for ch in username:
            if ch.isalpha() or ch.isdigit() or ch == "-" or ch == "_":
                pass
            else:
                is_valid = False
                break
        if is_valid:
            valid_usernames.append(username)

for valid_username in valid_usernames:
    print(valid_username)
