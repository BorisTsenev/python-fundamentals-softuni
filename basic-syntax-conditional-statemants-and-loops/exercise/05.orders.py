orders_count = int(input())
total_price = 0

for order in range(orders_count):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 <= capsule_price <= 100:
        if 1 <= days <= 31:
            if 1 <= capsules_per_day <= 2000:
                price = capsule_price * days * capsules_per_day
                total_price += price
                print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")