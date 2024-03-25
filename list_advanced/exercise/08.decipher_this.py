def decipher_this(sentence: list):
    deciphered_sentence = ""
    for word in sentence:
        first_letter_list = [x for x in word if x.isdigit()]
        first_letter_code = int(''.join(first_letter_list))
        first_letter = chr(first_letter_code)
        word = word.replace(str(first_letter_code), first_letter)
        word = [x for x in word]
        word[1], word[len(word) - 1] = word[len(word) - 1], word[1]
        word = ''.join(word)
        deciphered_sentence += word + " "

    return deciphered_sentence


cipher = input().split()
print(decipher_this(cipher))
