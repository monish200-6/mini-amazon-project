from storage import load_data, save_data

PRODUCTS_FILE = "products.json"

def list_products():
    products = load_data(PRODUCTS_FILE)
    for p in products:
        print(f"{p['product_id']} | {p['name']} | ${p['price']} | Stock: {p['stock']}")

def search_products():
    keyword = input("Search: ").lower()
    products = load_data(PRODUCTS_FILE)
    for p in products:
        if keyword in p["name"].lower():
            print(f"{p['product_id']} | {p['name']} | ${p['price']} | Stock: {p['stock']}")

def get_product(product_id):
    products = load_data(PRODUCTS_FILE)
    for p in products:
        if p["product_id"] == product_id:
            return p
    return None

def update_stock(product_id, new_stock):
    products = load_data(PRODUCTS_FILE)
    for p in products:
        if p["product_id"] == product_id:
            p["stock"] = new_stock
    save_data(PRODUCTS_FILE, products)