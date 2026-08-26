import re
import json
import os
if not os.path.exists("users.json"):
    with open("users.json", "w") as file:
        json.dump({}, file)


def load_users():
    with open("users.json", "r") as file:
        return json.load(file)


def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


def register():

    users = load_users()

    print("\n===== Register =====")

    try:

        name = input("Enter Full Name : ").strip()

        name_pattern = re.compile(r"^[A-Za-z ]+$")

        if not name_pattern.fullmatch(name):
            raise ValueError("Name should contain only letters.")

        email = input("Enter Email : ").strip()

        # match()
        email_pattern = re.compile(
            r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$"
        )

        if not email_pattern.match(email):
            raise ValueError("Invalid Email.")

        if email in users:
            raise ValueError("Email already registered.")

        phone = input("Enter Phone Number : ").strip()

        # fullmatch()
        if not re.fullmatch(r"[6-9]\d{9}", phone):
            raise ValueError("Invalid Phone Number.")

        password = input("Enter Password : ")

        # search()
        if not re.search(r"[A-Z]", password):
            raise ValueError(
                "Password needs an uppercase letter."
            )

        if not re.search(r"[a-z]", password):
            raise ValueError(
                "Password needs a lowercase letter."
            )

        if not re.search(r"\d", password):
            raise ValueError(
                "Password needs a number."
            )

        if not re.search(r"[@#$%^&*!]", password):
            raise ValueError(
                "Password needs a special character."
            )

        if len(password) < 8:
            raise ValueError(
                "Password must be at least 8 characters."
            )

        # sub()
        cleaned_name = re.sub(r"\s+", " ", name)

        users[email] = {
            "name": cleaned_name,
            "phone": phone,
            "password": password
        }

        save_users(users)

        print("\nRegistration Successful!")

    except Exception as e:
        print("Error :", e)


# Login
def login():

    users = load_users()

    print("\n===== Login =====")

    try:

        email = input("Enter Email : ").strip()
        password = input("Enter Password : ")

        if email not in users:
            raise ValueError("User not found.")

        if users[email]["password"] != password:
            raise ValueError("Incorrect Password.")

        print(f"\nWelcome {users[email]['name']}!")

        print("\nLogin Successful!")

        # Launch InventoryIQ
        import InventoryIQ_console.main as main
        main.start_inventory()

    except Exception as e:
        print("Error :", e)


# Regex Demonstration
def regex_demo():

    print("\n===== Regex Functions Demo =====")

    sample = "Stock1,Stock2,Stock3"

    # split()
    print("\nSplit Example")
    print(re.split(",", sample))

    text = "Item123 Product456 Inventory789"

    # findall()
    print("\nFindall Example")
    print(re.findall(r"\d+", text))


# Main Menu
while True:

    print("\n==============================")
    print("        InventoryIQ")
    print("==============================")
    print("1. Register")
    print("2. Login")
    print("3. Regex Demo")
    print("4. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        regex_demo()

    elif choice == "4":
        print("Thank you for using InventoryIQ!")
        break

    else:
        print("Invalid Choice.")