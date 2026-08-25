import requests


BASE_URL = "http://127.0.0.1:5000"


# Display all products
def get_all_products():

    try:

        response = requests.get(
            f"{BASE_URL}/products"
        )

        if response.status_code == 200:

            data = response.json()

            products = data.get("products", [])

            print("\n")
            print("=" * 60)
            print("              INVENTORY PRODUCTS")
            print("=" * 60)

            for product in products:

                print(f"Product ID     : {product.get('product_id')}")
                print(f"Product Name   : {product.get('product_name')}")
                print(f"Category       : {product.get('category')}")
                print(f"Stock          : {product.get('stock')}")
                print(f"Monthly Sales  : {product.get('monthly_sales')}")
                print("-" * 60)

            print(f"Total Products : {len(products)}")
            print("=" * 60)

        else:

            print(
                f"Error {response.status_code}: "
                f"{response.json().get('message', 'Unknown error')}"
            )

    except requests.ConnectionError:

        print(
            "\nConnection failed."
            "\nMake sure server.py is running."
        )

    except requests.RequestException as error:

        print("\nRequest error:", error)


# Get one product
def get_product():

    product_id = input(
        "Enter Product ID: "
    )

    try:

        response = requests.get(
            f"{BASE_URL}/products/{product_id}"
        )

        data = response.json()

        if response.status_code == 200:

            product = data["product"]

            print("\nProduct Found")
            print("----------------------------------------")
            print("ID       :", product["product_id"])
            print("Name     :", product["product_name"])
            print("Category :", product["category"])
            print("Stock    :", product["stock"])
            print("Sales    :", product["monthly_sales"])

        else:

            print(
                "Error:",
                data.get("message")
            )

    except requests.ConnectionError:

        print("Connection failed.")

    except requests.RequestException as error:

        print("Request error:", error)


# Add a product
def add_product():

    product = {
        "product_id": input("Product ID: "),
        "product_name": input("Product Name: "),
        "category": input("Category: "),
        "stock": int(input("Stock: ")),
        "monthly_sales": int(
            input("Monthly Sales: ")
        )
    }

    try:

        response = requests.post(
            f"{BASE_URL}/products",
            json=product
        )

        data = response.json()

        if response.status_code == 201:

            print(
                "\nSuccess:",
                data["message"]
            )

        else:

            print(
                "\nError:",
                data.get("message")
            )

    except ValueError:

        print(
            "Stock and Monthly Sales "
            "must be numbers."
        )

    except requests.ConnectionError:

        print("Connection failed.")

    except requests.RequestException as error:

        print("Request error:", error)


# Update a product
def update_product():

    product_id = input(
        "Enter Product ID to update: "
    )

    print("\nLeave a field blank to keep it unchanged.")

    product_name = input(
        "New Product Name: "
    )

    category = input(
        "New Category: "
    )

    stock = input(
        "New Stock: "
    )

    monthly_sales = input(
        "New Monthly Sales: "
    )

    update_data = {}

    if product_name:
        update_data["product_name"] = product_name

    if category:
        update_data["category"] = category

    if stock:
        update_data["stock"] = int(stock)

    if monthly_sales:
        update_data["monthly_sales"] = int(
            monthly_sales
        )

    try:

        response = requests.put(
            f"{BASE_URL}/products/{product_id}",
            json=update_data
        )

        data = response.json()

        if response.status_code == 200:

            print(
                "\nSuccess:",
                data["message"]
            )

            print(
                "Updated Product:",
                data["product"]
            )

        else:

            print(
                "\nError:",
                data.get("message")
            )

    except ValueError:

        print(
            "Stock and Monthly Sales "
            "must be numbers."
        )

    except requests.ConnectionError:

        print("Connection failed.")

    except requests.RequestException as error:

        print("Request error:", error)


# Delete a product
def delete_product():

    product_id = input(
        "Enter Product ID to delete: "
    )

    try:

        response = requests.delete(
            f"{BASE_URL}/products/{product_id}"
        )

        data = response.json()

        if response.status_code == 200:

            print(
                "\nSuccess:",
                data["message"]
            )

        else:

            print(
                "\nError:",
                data.get("message")
            )

    except requests.ConnectionError:

        print("Connection failed.")

    except requests.RequestException as error:

        print("Request error:", error)


# Main client menu
while True:

    print("\n========================================")
    print("        InventoryIQ API Client")
    print("========================================")

    print("1. View All Products")
    print("2. View Product")
    print("3. Add Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Exit")

    choice = input(
        "\nEnter Choice: "
    )

    if choice == "1":

        get_all_products()

    elif choice == "2":

        get_product()

    elif choice == "3":

        add_product()

    elif choice == "4":

        update_product()

    elif choice == "5":

        delete_product()

    elif choice == "6":

        print(
            "\nThank you for using InventoryIQ!"
        )

        break

    else:

        print(
            "\nInvalid choice. Please try again."
        )