fires = input().split("#")
water_count = int(input())
total_effort = 0
total_fire = 0
print("Cells:")

for current_fire in range(len(fires)):
    fire = fires[current_fire].split(" = ")
    type_of_fire = fire[0]
    fire_value = int(fire[1])
    is_valid = type_of_fire == "Low" and 1 <= fire_value <= 50 \
               or type_of_fire == "Medium" and 51 <= fire_value <= 80 \
               or type_of_fire == "High" and 81 <= fire_value <= 125

    have_enough_water = water_count >= fire_value

    if is_valid and have_enough_water:
        total_fire += fire_value
        total_effort += 0.25 * fire_value
        water_count -= fire_value
        print(f" - {fire_value}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
