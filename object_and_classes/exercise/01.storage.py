class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = list()

    def add_product(self, product):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage


storage = Storage(2)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
storage.add_product("kur")
storage.add_product("madur")

print(storage.get_products())
