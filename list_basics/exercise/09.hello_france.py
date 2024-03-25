items = input().split("|")
budget = float(input())
total_profit = 0
money_made = 0

for current_sell in range(len(items)):
    current_item = items[current_sell].split("->")
    product_type = current_item[0]
    product_price = float(current_item[1])

    is_valid = product_type == "Clothes" and product_price <= 50 \
               or product_type == "Shoes" and product_price <= 35 \
               or product_type == "Accessories" and product_price <= 20.5

    have_enough_money = budget >= product_price

    if is_valid and have_enough_money:
        budget -= product_price
        profit = 0.4 * product_price
        total_profit += profit
        money_made += profit + product_price
        print(f"{(profit + product_price):.2f} ", end="")


print(f"\nProfit: {total_profit:.2f}")
if total_profit + money_made + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
