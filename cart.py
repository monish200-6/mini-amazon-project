from storage import load_data, save_data
from products import get_product

CART_FILE = "carts.json"

def get_cart(username):
    carts = load_data(CART_FILE)
    for c in carts:
        if c["username"] == username:
            return c
    return {"username": username, "items": []}

def save_cart(cart):
    carts = load_data(CART_FILE)
    carts = [c for c in carts if c["username"] != cart["username"]]
    carts.append(cart)
    save_data(CART_FILE, carts)

def add_to_cart(username):
    cart = get_cart(username)
    product_id = input("Enter product ID: ")
    qty = int(input("Enter quantity: "))

    product = get_product(product_id)
    if not product:
        print("Product not found.")
        return

    if qty <= 0 or qty > product["stock"]:
        print("Invalid quantity.")
        return

    cart["items"].append({
        "product_id": product_id,
        "quantity": qty
    })

    save_cart(cart)
    print("Added to cart.")

def view_cart(username):
    cart = get_cart(username)
    total = 0

    for item in cart["items"]:
        product = get_product(item["product_id"])
        subtotal = product["price"] * item["quantity"]
        total += subtotal
        print(f"{product['name']} | {item['quantity']} | ${subtotal}")

    print("Total:", total)

def clear_cart(username):
    save_cart({"username": username, "items": []})