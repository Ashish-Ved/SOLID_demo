class Order:
    def __init__(self, items: list):
        self.items = items  # list of (name, price)

    def calculate_total(self):
        return sum(price for _, price in self.items)
