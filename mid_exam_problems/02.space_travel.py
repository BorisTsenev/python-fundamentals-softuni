def travel(total_fuel, light_years):
    if light_years > total_fuel:
        return False
    else:

        return total_fuel - light_years


def enemy(total_ammo, enemy_armour, total_fuel):
    if total_ammo >= enemy_armour:
        print(f"An enemy with {enemy_armour} armour is defeated.")
        return total_ammo - enemy_armour
    else:
        total_fuel = travel(total_fuel, enemy_armour * 2)
        if not total_fuel:
            print("Mission failed.")
            return False
        else:
            print(f"An enemy with {enemy_armour} armour is outmaneuvered.")
            return total_fuel


titan_travel_route = input().split("||")
titan_travel_commands = [command.split() for command in titan_travel_route]
fuel = int(input())
ammo = int(input())

for command in titan_travel_commands:
    if command[0] == "Travel":
        fuel = travel(fuel, int(command[1]))
        if not fuel:
            print("Mission failed.")
            break
        else:
            print(f"The spaceship travelled {int(command[1])} light-years.")
    elif command[0] == "Enemy":
        if ammo >= int(command[1]):
            ammo = enemy(ammo, int(command[1]), fuel)
        else:
            fuel = enemy(ammo, int(command[1]), fuel)
        if not fuel:
            break
    elif command[0] == "Repair":
        ammo += int(command[1]) * 2
        fuel += int(command[1])
        print(f"Ammunitions added: {int(command[1]) * 2}.\nFuel added: {int(command[1])}.")
    elif command[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
