random_words = input().lower()

is_sand = random_words.find("sand")
is_water = random_words.find("water")
is_fish = random_words.find("fish")
is_sun = random_words.find("sun")
word_count = 0

if is_sun != -1:
    word_count += 1

if is_fish != -1:
    word_count += 1

if is_water != -1:
    word_count += 1

if is_sand != -1:
    word_count += 1

print(word_count)