day_actions = input().split("|")
coins = 100
energy = 100
not_failed = True

for current_action in range(len(day_actions)):
    action = day_actions[current_action].split("-")
    action_type = action[0]
    action_points = int(action[1])
    have_enough_energy = energy > 30
    have_enough_coins = coins > action_points

    if action_type == "rest":
        if energy + action_points > 100:
            gained_energy = 100 - energy
        else:
            gained_energy = action_points
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif action_type == "order":
        if have_enough_energy:
            coins += action_points
            energy -= 30
            print(f"You earned {action_points} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if have_enough_coins:
            coins -= action_points
            print(f"You bought {action_type}.")
        else:
            print(f"Closed! Cannot afford {action_type}.")
            not_failed = False
            break
if not_failed:
    print(f"Day completed! \nCoins: {coins} \nEnergy: {energy}")
