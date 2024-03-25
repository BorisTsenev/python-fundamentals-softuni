def is_palindrome(word):
    letters_forward = [k for k in word]
    letters_backward = list(reversed(letters_forward))

    if letters_forward == letters_backward:
        return True
    else:
        return False


words = input().split()
searched_palindrome = input()

palindrome_words = list(filter(is_palindrome, words))
searched_palindrome_count = palindrome_words.count(searched_palindrome)
print(palindrome_words)
print(f"Found palindrome {searched_palindrome_count} times")
