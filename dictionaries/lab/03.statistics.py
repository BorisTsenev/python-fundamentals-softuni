products_and_quantities = dict()
while True:
    command = input()
    if command == "statistics":
        break
    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])
    if product in products_and_quantities.keys():
        products_and_quantities[product] += quantity
    else:
        products_and_quantities[product] = quantity

quantity_sum = 0
product_count = 0
print("Products in stock:")
for (product, quantity) in products_and_quantities.items():
    quantity_sum += quantity
    product_count += 1
    print(f"- {product}: {quantity}")

print(f"Total Products: {product_count}\nTotal Quantity: {quantity_sum}")
