from flask import Flask, request, render_template
from services.order_service import OrderService
from services.discount import FixedDiscount
from services.notification import EmailSender
from services.repository import OrderRepository

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        item1 = request.form['item1']
        price1 = float(request.form['price1'])
        item2 = request.form['item2']
        price2 = float(request.form['price2'])

        order_items = [(item1, price1), (item2, price2)]

        service = OrderService(FixedDiscount(), OrderRepository(), EmailSender())
        total, discounted = service.process_order(order_items)

        return f"Total: {total}, After Discount: {discounted}"

    return render_template('order_form.html')

if __name__ == '__main__':
    app.run(debug=True)
