input_products = input().split()
products = [input_products[i] for i in range(len(input_products)) if i % 2 == 0]
quantities = [int(input_products[i]) for i in range(len(input_products)) if i % 2 == 1]
products_and_quantities = dict(zip(products, quantities))

searched_products = input().split()

for search_product in searched_products:
    if products_and_quantities.get(search_product) is None:
        print(f"Sorry, we don't have {search_product}")
    else:
        print(f"We have {products_and_quantities.get(search_product)} of {search_product} left")
