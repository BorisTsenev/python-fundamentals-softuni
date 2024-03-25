def password_validator(password):
    def is_between(a):
        b = len(a)
        if 6 <= b <= 10:
            return ""
        else:
            return "Password must be between 6 and 10 characters\n"

    def is_only_of_letter_and_digit(a):

        for char in a:
            if ord(char) in range(48, 59) \
               or ord(char) in range(65, 91) \
               or ord(char) in range(97, 123):
                pass
            else:
                return "Password must consist only of letters and digits\n"
        return ""

    def have_two_digits(a):
        digit_count = 0
        for char in a:
            if ord(char) in range(48, 59):
                digit_count += 1

        if digit_count < 2:
            return "Password must have at least 2 digits"
        else:
            return ""

    output_return = is_between(password) + is_only_of_letter_and_digit(password) + have_two_digits(password)
    if output_return != "":
        return output_return
    else:
        return "Password is valid"


password = input()

print(password_validator(password))
