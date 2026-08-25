from flask import Flask, jsonify, request
import json
import os


app = Flask(__name__)

DATA_FILE = "inventory.json"


# Load products from JSON
def load_products():

    try:

        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:

        return []

    except json.JSONDecodeError:

        return []


# Save products to JSON
def save_products(products):

    with open(DATA_FILE, "w") as file:
        json.dump(products, file, indent=4)


# GET all products
@app.route("/products", methods=["GET"])
def get_products():

    products = load_products()

    return jsonify({
        "success": True,
        "count": len(products),
        "products": products
    }), 200


# GET one product
@app.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):

    products = load_products()

    for product in products:

        if product["product_id"] == product_id:

            return jsonify({
                "success": True,
                "product": product
            }), 200

    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404


# POST a new product
@app.route("/products", methods=["POST"])
def add_product():

    data = request.get_json()

    if not data:

        return jsonify({
            "success": False,
            "message": "Request must contain JSON data"
        }), 400

    required_fields = [
        "product_id",
        "product_name",
        "category",
        "stock",
        "monthly_sales"
    ]

    for field in required_fields:

        if field not in data:

            return jsonify({
                "success": False,
                "message": f"Missing field: {field}"
            }), 400

    products = load_products()

    # Check for duplicate ID
    for product in products:

        if product["product_id"] == data["product_id"]:

            return jsonify({
                "success": False,
                "message": "Product ID already exists"
            }), 409

    new_product = {
        "product_id": data["product_id"],
        "product_name": data["product_name"],
        "category": data["category"],
        "stock": data["stock"],
        "monthly_sales": data["monthly_sales"]
    }

    products.append(new_product)

    save_products(products)

    return jsonify({
        "success": True,
        "message": "Product added successfully",
        "product": new_product
    }), 201


# PUT an existing product
@app.route("/products/<product_id>", methods=["PUT"])
def update_product(product_id):

    data = request.get_json()

    if not data:

        return jsonify({
            "success": False,
            "message": "Request must contain JSON data"
        }), 400

    products = load_products()

    for product in products:

        if product["product_id"] == product_id:

            if "product_name" in data:
                product["product_name"] = data["product_name"]

            if "category" in data:
                product["category"] = data["category"]

            if "stock" in data:
                product["stock"] = data["stock"]

            if "monthly_sales" in data:
                product["monthly_sales"] = data["monthly_sales"]

            save_products(products)

            return jsonify({
                "success": True,
                "message": "Product updated successfully",
                "product": product
            }), 200

    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404


# DELETE a product
@app.route("/products/<product_id>", methods=["DELETE"])
def delete_product(product_id):

    products = load_products()

    for product in products:

        if product["product_id"] == product_id:

            products.remove(product)

            save_products(products)

            return jsonify({
                "success": True,
                "message": "Product deleted successfully"
            }), 200

    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404


# Handle unknown URLs
@app.errorhandler(404)
def page_not_found(error):

    return jsonify({
        "success": False,
        "message": "Endpoint not found"
    }), 404


# Start the server
if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )