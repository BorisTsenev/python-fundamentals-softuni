money_list = input().split(", ")
beggars_count = int(input())
output_list = []

for current_beggar in range(beggars_count):
    current_beggar_sum = 0
    for current_money in range(current_beggar, len(money_list), beggars_count):
        current_beggar_sum += int(money_list[current_money])
    output_list.append(current_beggar_sum)

print(output_list)
