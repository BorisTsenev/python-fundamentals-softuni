def is_palindrome(x):
    y = str(x)
    list_of_digits = list()
    for i in range(len(y)):
        list_of_digits.append(y[i])

    if list_of_digits == list(reversed(list_of_digits)):
        return True
    else:
        return False


numbers = list(map(int, input().split(", ")))

for number in numbers:
    print(is_palindrome(number))
