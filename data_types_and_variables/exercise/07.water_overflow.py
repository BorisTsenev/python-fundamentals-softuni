pour_count = int(input())
litters_in_water_tank = 0

for pour in range(pour_count):
    current_pour = int(input())

    if current_pour + litters_in_water_tank > 255:
        print("Insufficient capacity!")

    else:
        litters_in_water_tank += current_pour

print(litters_in_water_tank)
