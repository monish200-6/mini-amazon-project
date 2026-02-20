# Mini Amazon - Console Based E-Commerce System

## Course
Programming with Python

## Project Description
This project is a console-based e-commerce system similar to Amazon.
Users can register, login, browse products, add items to cart, and checkout.

The system uses JSON files for data persistence.

---

## How To Run

1. Open the project folder in VS Code
2. Open terminal
3. Run the following command:

   python main.py

type 1 registration
type 2 login
type 3 Browse products
type 4 add to cart
type 5 view cart 
type 6 checkout
---

## Features Implemented

- User Registration
- User Login
- Password Hashing (SHA-256)
- Product Catalog
- Product Search (case-insensitive)
- Shopping Cart System
- Checkout System
- Order History Storage
- Stock Validation
- Receipt Export to Text File
- Admin Mode (Add and Update Products)

---

## File Structure

main.py - Main program
users.py - User management
products.py - Product catalog
cart.py - Cart system
orders.py - Checkout and order storage
admin.py - Admin functionality
storage.py - File handling
users.json - Stores user data
products.json - Stores product data
carts.json - Stores cart data
orders.json - Stores order history

---

## Data Storage

All data is stored using JSON files.
This ensures data persistence even after restarting the program.

---

## Bonus Features Implemented

- Password hashing using hashlib
- Admin mode for managing products
- Receipt export to text file

---

## Known Limitations

- Console-based UI
- No payment gateway integration
- No graphical interface

---

## Author

Student Name: (MONISH CHOPRA)
Student ID: (100007201)