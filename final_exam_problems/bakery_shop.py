def receive(foods_and_quantities: dict, quantity, food):
    if quantity > 0:
        if food not in foods_and_quantities.keys():
            foods_and_quantities[food] = 0
        foods_and_quantities[food] += quantity
    return foods_and_quantities

def sell(foods_and_quantities: dict, quantity, food, sold_food_count):
    if food not in foods_and_quantities.keys():
        print(f"You do not have any {food}.")
    else:
        if quantity > foods_and_quantities[food]:
            sold_food_count += foods_and_quantities[food]
            foods_and_quantities.pop(food)
            print(f"There aren't enough {food}. You sold the last {quantity} of them.")
        else:
            foods_and_quantities[food] -= quantity
            sold_food_count += quantity
            print(f"You sold {quantity} {food}.")

    return foods_and_quantities, sold_food_count

foods_and_quantities = {}
sold_food_quantity = 0

while True:
    command = input()
    if command == "Complete":
        for (food, quantity) in foods_and_quantities.items():
            if quantity > 0:
                print(f"{food}: {quantity}")
        print(f"All sold: {sold_food_quantity} goods")
        break
    action, quantity, food = command.split()
    action = action.lower()
    if action == "sell":
        foods_and_quantities, sold_food_quantity = sell(foods_and_quantities, int(quantity), food, sold_food_quantity)
    else:
        foods_and_quantities = receive(foods_and_quantities, int(quantity), food)
