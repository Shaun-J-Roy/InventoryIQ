import requests


# Fetch products from the public API
def fetch_products():

    url = "https://fakestoreapi.com/products"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return response.json()

    except requests.RequestException:
        return []


# Process the API data
def process_products(products):

    if not products:
        return "No product data available."

    total_products = len(products)
    total_price = 0
    categories = {}

    for product in products:

        # Use get() to safely access dictionary values
        price = product.get("price", 0)
        category = product.get("category", "Unknown")

        total_price += price

        # Count products in each category
        categories[category] = (
            categories.get(category, 0) + 1
        )

    average_price = total_price / total_products

    result = "API PRODUCT DATA\n"
    result += "=" * 35 + "\n\n"

    # Display the first five products
    for product in products[:5]:

        rating = product.get("rating", {})

        result += f"ID: {product.get('id')}\n"
        result += f"Product: {product.get('title')}\n"
        result += f"Price: ${product.get('price'):.2f}\n"
        result += f"Category: {product.get('category')}\n"
        result += f"Rating: {rating.get('rate', 'N/A')}\n"
        result += f"Reviews: {rating.get('count', 'N/A')}\n"
        result += "-" * 35 + "\n"

    result += "\nSUMMARY\n"
    result += "=" * 35 + "\n"
    result += f"Total Products: {total_products}\n"
    result += f"Average Price: ${average_price:.2f}\n"

    result += "\nPRODUCTS BY CATEGORY\n"

    for category, count in categories.items():
        result += f"{category}: {count}\n"

    return result


# Demonstrate dictionary functions
def dictionary_demo(products):

    if not products:
        return {}

    product = products[0]

    return {
        "keys": list(product.keys()),
        "values": list(product.values()),
        "items": list(product.items()),
        "product_name": product.get("title"),
        "price": product.get("price")
    }
