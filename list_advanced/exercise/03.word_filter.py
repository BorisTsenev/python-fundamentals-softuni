def word_even_filter(input_sequence):
    input_list = input_sequence.split()
    filtered_list = [x for x in input_list if len(x) % 2 == 0]
    return '\n'.join(filtered_list)


word_list = input()
print(word_even_filter(word_list))
