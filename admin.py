from storage import load_data, save_data

PRODUCTS_FILE = "products.json"

def admin_menu():
    print("1. Add product")
    print("2. Update stock")
    choice = input("Choice: ")

    products = load_data(PRODUCTS_FILE)

    if choice == "1":
        pid = input("Product ID: ")
        name = input("Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))

        products.append({
            "product_id": pid,
            "name": name,
            "price": price,
            "stock": stock
        })

        save_data(PRODUCTS_FILE, products)

    elif choice == "2":
        pid = input("Product ID: ")
        for p in products:
            if p["product_id"] == pid:
                p["stock"] = int(input("New stock: "))
        save_data(PRODUCTS_FILE, products)