input_products = input().split()
products = [input_products[i] for i in range(len(input_products)) if i % 2 == 0]
quantities = [int(input_products[i]) for i in range(len(input_products)) if i % 2 == 1]
products_and_quantities = dict(zip(products, quantities))

print(products_and_quantities)
