from .order import Order

class OrderService:
    def __init__(self, discount_strategy, repository, notifier):
        self.discount_strategy = discount_strategy
        self.repository = repository
        self.notifier = notifier

    def process_order(self, items):
        order = Order(items)
        total = order.calculate_total()
        discounted = self.discount_strategy.apply(total)
        self.repository.save(order)
        self.notifier.send(f"Order placed for ${discounted}")
        return total, discounted
