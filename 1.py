import re
import os

FILE_NAME = "users.txt"

# ---------------- USERNAME VALIDATION ----------------
def validate_username(username):
    if not re.match(r'^[a-zA-Z]', username):
        return False
    if "@" not in username or "." not in username:
        return False
    at_pos = username.index("@")
    dot_pos = username.rindex(".")
    if dot_pos < at_pos + 2:
        return False
    return True


# ---------------- PASSWORD VALIDATION ----------------
def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+=-]", password):
        return False
    return True


# ---------------- REGISTRATION ----------------
def register():
    username = input("Enter username (email): ")
    if not validate_username(username):
        print("❌ Invalid username format")
        return

    password = input("Enter password: ")
    if not validate_password(password):
        print("❌ Weak password")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{username}:{password}\n")

    print("✅ Registration successful")


# ---------------- LOGIN ----------------
def login():
    if not os.path.exists(FILE_NAME):
        print("No users registered yet.")
        return

    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(FILE_NAME, "r") as file:
        users = file.readlines()

    for user in users:
        stored_user, stored_pass = user.strip().split(":")
        if username == stored_user and password == stored_pass:
            print("✅ Login successful")
            return

    print("❌ Invalid credentials")
    forgot_option()


# ---------------- FORGOT PASSWORD ----------------
def forgot_option():
    choice = input("Forgot password? (yes/no): ").lower()
    if choice != "yes":
        return

    username = input("Enter your username: ")

    with open(FILE_NAME, "r") as file:
        users = file.readlines()

    for i, user in enumerate(users):
        stored_user, stored_pass = user.strip().split(":")
        if username == stored_user:
            print(f"🔑 Your password is: {stored_pass}")
            return

    print("Username not found. Please register.")


# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()
