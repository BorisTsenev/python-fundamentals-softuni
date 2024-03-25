input = input()

list = input.split(", ")

if len(list) - 1 == list.index("wolf"):
    print("Please go away and stop eating my sheep")
else:
    sheep_num = len(list) - (list.index("wolf") + 1)
    print(f"Oi! Sheep number {sheep_num}! You are about to be eaten by a wolf!")
