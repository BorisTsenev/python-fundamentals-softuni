input_cards = input()
shuffle_count = int(input())
cards_list = input_cards.split()


middle_of_the_deck = int(len(cards_list) / 2)

for current_shuffle in range(shuffle_count):
    shuffling_list = list()
    first_half = cards_list[:middle_of_the_deck]
    second_half = cards_list[middle_of_the_deck::]
    shuffling_list.append(cards_list[0])

    for i in range(1, middle_of_the_deck):
        shuffling_list.append(second_half[i - 1])
        shuffling_list.append(first_half[i])

    shuffling_list.append(cards_list[len(cards_list) - 1])
    cards_list = shuffling_list

print(cards_list)
