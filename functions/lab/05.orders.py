def calculate_order(product, count):
    if product == "water":
        return f"{(count * 1.0):.2f}"
    elif product == "coke":
        return f"{(count * 1.4):.2f}"
    elif product == "coffee":
        return f"{(count * 1.5):.2f}"
    elif product == "snacks":
        return f"{(count * 2.0):.2f}"


ordered_product = input()
product_count = int(input())

print(calculate_order(ordered_product, product_count))
