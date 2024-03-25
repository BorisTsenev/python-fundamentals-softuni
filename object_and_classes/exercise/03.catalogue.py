class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = list()

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        output = [x for x in self.products if x[0] == first_letter]
        return output

    def __repr__(self):
        output = f"Items in the {self.name} catalogue:"
        sorted_products = sorted(self.products)
        for product in sorted_products:
            output += f"\n{product}"

        return output


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
