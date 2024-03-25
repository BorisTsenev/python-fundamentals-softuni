quantity_of_decorations = int(input())
days_left = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

spirit = 0
total_cost = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        total_cost += ornament_set_price * quantity_of_decorations
        spirit += 5

    if day % 3 == 0:
        total_cost += quantity_of_decorations * (tree_garland_price + tree_skirt_price)
        spirit += 10 + 3

    if day % 5 == 0:
        total_cost += tree_lights_price * quantity_of_decorations
        spirit += 17
        if day % 3 == 0:
            spirit += 30

    if day % 10 == 0:
        total_cost += tree_lights_price + tree_skirt_price + tree_garland_price
        spirit -= 20

if days_left % 10 == 0:
    spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")
