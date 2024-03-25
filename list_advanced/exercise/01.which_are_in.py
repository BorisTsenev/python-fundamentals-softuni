def which_are_in(first_sequence, second_sequence):
    string_to_search = first_sequence.split(", ")
    searched_string = second_sequence.split(", ")
    found_items = list()
    for i in range(len(string_to_search)):
        for j in range(len(searched_string)):
            if string_to_search[i] in searched_string[j]:
                found_items.append(string_to_search[i])
    output_list = list()
    [output_list.append(x) for x in found_items if x not in output_list]
    return output_list


searching_items = input()
searched_items = input()

print(which_are_in(searching_items, searched_items))
