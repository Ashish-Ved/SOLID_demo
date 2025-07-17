from order import Order
from discount import FixedDiscount
from repository import OrderRepository
from notification import EmailSender

items = [("Keyboard", 100), ("Mouse", 50)]

order = Order(items)
repository = OrderRepository()
discount = FixedDiscount()
notifier = EmailSender()

total = order.calculate_total()
discounted = discount.apply(total)

print(f"Original Total: {total}")
print(f"Discounted Total: {discounted}")

repository.save(order)
notifier.send(f"Your order of ${discounted} has been processed.")
