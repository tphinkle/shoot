class FactoryComponent():
    def __init__(self):
        self.orders = []

        self.num_products = 0


        pass

class Order():
    def __init__(self, name, on_creation):
        self.name = name
        self.on_creation = on_creation
