from math import floor

group_size = int(input())
days = int(input())
coins_count = 0

for day in range(1, days + 1):
    coins_count += 50
    coins_count -= 2 * group_size

    if day % 10 == 0:
        group_size -= 2
        if group_size < 0:
            group_size = 0

    if day % 15 == 0:
        group_size += 5

    if day % 3 == 0:
        coins_count -= 3 * group_size

    if day % 5 == 0:
        coins_count += 20 * group_size

        if day % 3 == 0:

            coins_count -= 2 * group_size

if not group_size == 0:
    print(f"{group_size} companions received {floor(coins_count / group_size)} coins each.")
else:
    print(f"{group_size} companions received {coins_count} coins each.")
