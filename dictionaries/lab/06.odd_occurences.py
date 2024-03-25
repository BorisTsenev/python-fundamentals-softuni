words_sequence = input().split()
words_sequence = [x.lower() for x in words_sequence]
words = list(dict.fromkeys(words_sequence))
words_count = {}

for word in words:
    words_count[word] = words_sequence.count(word)

for (word, count) in words_count.items():
    if count % 2 == 1:
        print(word, end=" ")
