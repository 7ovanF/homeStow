class ItemCollection:
    def __init__(self):
        self.products = dict()
        self.index()

    def add_item(self, item):
        self.products += item

    def __add__(self, other):
        """ItemCollection + another ItemCollection btw"""
        a
        return

    def __iter__(self):
#         if class has __next__ u just return self.
#         however, this is just for example of a GENERATOR
        for product, price in self.products.items():
            yield (product, price)

    def __next__(self):


