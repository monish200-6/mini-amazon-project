import hashlib
from storage import load_data, save_data

USERS_FILE = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    users = load_data(USERS_FILE)
    username = input("Enter username: ")

    if any(u["username"] == username for u in users):
        print("Username already exists.")
        return None

    password = input("Enter password (min 6 chars): ")
    if len(password) < 6:
        print("Password too short.")
        return None

    users.append({
        "username": username,
        "password": hash_password(password),
        "role": "user"
    })

    save_data(USERS_FILE, users)
    print("Registration successful.")
    return username

def login():
    users = load_data(USERS_FILE)
    username = input("Username: ")
    password = hash_password(input("Password: "))

    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login successful.")
            return user

    print("Invalid credentials.")
    return None