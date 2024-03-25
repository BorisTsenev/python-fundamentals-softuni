synonyms_count = int(input())
synonyms = {}

for _ in range(synonyms_count):
    word = input()
    synonym = input()

    if word in synonyms.keys():
        synonyms[word].append(synonym)
    else:
        synonyms[word] = synonym.split()

for (word, synonym) in synonyms.items():
    print(f"{word} - {', '.join(synonym)}")
