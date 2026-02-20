from storage import load_data, save_data
from products import get_product, update_stock
from cart import get_cart, clear_cart
from datetime import datetime
import uuid

ORDERS_FILE = "orders.json"

def checkout(username):
    cart = get_cart(username)
    if not cart["items"]:
        print("Cart is empty.")
        return

    total = 0
    items_summary = []

    for item in cart["items"]:
        product = get_product(item["product_id"])

        if item["quantity"] > product["stock"]:
            print("Stock issue.")
            return

        subtotal = product["price"] * item["quantity"]
        total += subtotal

        update_stock(product["product_id"], product["stock"] - item["quantity"])

        items_summary.append({
            "product_id": product["product_id"],
            "qty": item["quantity"],
            "unit_price": product["price"]
        })

    order = {
        "order_id": str(uuid.uuid4())[:8],
        "username": username,
        "items": items_summary,
        "total": total,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    orders = load_data(ORDERS_FILE)
    orders.append(order)
    save_data(ORDERS_FILE, orders)

    export_receipt(order)

    clear_cart(username)
    print("Checkout successful.")

def export_receipt(order):
    filename = f"receipt_{order['order_id']}.txt"
    with open(filename, "w") as f:
        f.write("Mini Amazon Receipt\n")
        f.write(str(order))