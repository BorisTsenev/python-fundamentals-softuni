adventure_days = int(input())
players_count = int(input())
group_energy = float(input())
# this is for one person ->
water_per_day = float(input())
food_per_day = float(input())
total_water = adventure_days * water_per_day * players_count
total_food = food_per_day * players_count * adventure_days
current_day = 0
while True:
    current_day += 1
    if current_day == adventure_days + 1:
        break
    energy_loss = float(input())
    group_energy -= energy_loss

    if current_day % 2 == 0:
        group_energy *= 1.05
        total_water *= 0.7

    if current_day % 3 == 0:
        total_food -= total_food / players_count
        group_energy *= 1.1

    if group_energy <= 0:


if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")

