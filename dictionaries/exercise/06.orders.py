products = {}
while True:
    command = input()
    if command == "buy":
        break

    product, price, quantity = command.split()
    money = [float(price), float(quantity)]
    if product in products.keys():
        products[product][0] = money[0]
        products[product][1] += money[1]
    else:
        products[product] = money

for (product, money) in products.items():
    print(f"{product} -> {(money[0] * money[1]):.2f}")
