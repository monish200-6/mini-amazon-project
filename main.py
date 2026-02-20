from users import register, login
from products import list_products, search_products
from cart import add_to_cart, view_cart
from orders import checkout
from admin import admin_menu

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\n1. Browse\n2. Search\n3. Add to cart\n4. View cart\n5. Checkout\n6. Admin\n7. Logout")
                    c = input("Choice: ")

                    if c == "1":
                        list_products()
                    elif c == "2":
                        search_products()
                    elif c == "3":
                        add_to_cart(user["username"])
                    elif c == "4":
                        view_cart(user["username"])
                    elif c == "5":
                        checkout(user["username"])
                    elif c == "6" and user.get("role") == "admin":
                        admin_menu()
                    elif c == "7":
                        break

        elif choice == "3":
            break

if __name__ == "__main__":
    main()