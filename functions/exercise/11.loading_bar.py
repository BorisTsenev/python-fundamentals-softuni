def loading_bar(a):
    loaded_tens = int(a / 10)
    loaded_bar = "[" + loaded_tens * "%" + (10 - loaded_tens) * "." + "]"

    if a == 100:
        return f"{a}% Complete!\n" \
               f"{loaded_bar}"
    else:
        return f"{a}% {loaded_bar}\n" \
                "Still loading..."


loaded = int(input())

print(loading_bar(loaded))
