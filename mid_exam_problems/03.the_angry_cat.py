def calculate_damage(items, entry_point, item_type):
    left_damage = 0
    right_damage = 0

    if item_type == "cheap":
        for i in range(entry_point):
            if items[i] < items[entry_point]:
                left_damage += items[i]
        for i in range(entry_point + 1, len(items)):
            if items[i] < items[entry_point]:
                right_damage += items[i]
    elif item_type == "expensive":
        for i in range(entry_point):
            if items[i] >= items[entry_point]:
                left_damage += items[i]
        for i in range(entry_point + 1, len(items)):
            if items[i] >= items[entry_point]:
                right_damage += items[i]

    max_damage = max(left_damage, right_damage)
    position = "Left" if left_damage >= right_damage else "Right"

    print(f"{position} - {max_damage}")

# Input
prices = list(map(int, input().split(", ")))
entry_point = int(input())
item_type = input()

# Calculate and output the result
calculate_damage(prices, entry_point, item_type)
