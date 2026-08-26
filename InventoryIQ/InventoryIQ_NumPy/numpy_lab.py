import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Load CSV dataset
try:

    df = pd.read_csv("inventory_numpy.csv")

except FileNotFoundError:

    print("Error: inventory_numpy.csv not found.")
    exit()


# Create NumPy arrays
stock = df["Stock"].to_numpy()
sales = df["Monthly_Sales"].to_numpy()
prices = df["Price"].to_numpy()


# ============================================================
# 1. COMPUTATION WITH NUMPY
# ============================================================

def numpy_computation():

    print("\n" + "=" * 60)
    print("COMPUTATION WITH NUMPY")
    print("=" * 60)

    print("\nStock Array:")
    print(stock)

    print("\nMonthly Sales Array:")
    print(sales)

    print("\nPrice Array:")
    print(prices)

    # Basic arithmetic
    stock_plus_sales = stock + sales

    sales_difference = stock - sales

    revenue = sales * prices

    print("\nStock + Monthly Sales:")
    print(stock_plus_sales)

    print("\nStock - Monthly Sales:")
    print(sales_difference)

    print("\nEstimated Monthly Revenue:")
    print(revenue)


# ============================================================
# 2. AGGREGATIONS
# ============================================================

def aggregations():

    print("\n" + "=" * 60)
    print("NUMPY AGGREGATIONS")
    print("=" * 60)

    print("\nTotal Stock:")
    print(np.sum(stock))

    print("\nTotal Monthly Sales:")
    print(np.sum(sales))

    print("\nAverage Stock:")
    print(np.mean(stock))

    print("\nAverage Monthly Sales:")
    print(np.mean(sales))

    print("\nMaximum Stock:")
    print(np.max(stock))

    print("\nMinimum Stock:")
    print(np.min(stock))

    print("\nMaximum Monthly Sales:")
    print(np.max(sales))

    print("\nMinimum Monthly Sales:")
    print(np.min(sales))

    print("\nStandard Deviation of Stock:")
    print(np.std(stock))


# ============================================================
# 3. COMPUTATION ON ARRAYS
# ============================================================

def array_operations():

    print("\n" + "=" * 60)
    print("COMPUTATION ON ARRAYS")
    print("=" * 60)

    # Stock turnover
    turnover = sales / stock

    # Remaining stock after one month
    remaining_stock = stock - sales

    # 10% increase in sales
    increased_sales = sales * 1.10

    # 5% discount on prices
    discounted_prices = prices * 0.95

    print("\nStock Turnover:")
    print(
        np.round(turnover, 2)
    )

    print("\nRemaining Stock After Monthly Sales:")
    print(remaining_stock)

    print("\nMonthly Sales After 10% Increase:")
    print(
        np.round(increased_sales, 2)
    )

    print("\nPrices After 5% Discount:")
    print(
        np.round(discounted_prices, 2)
    )


# ============================================================
# 4. COMPARISONS, MASKS AND BOOLEAN ARRAYS
# ============================================================

def comparisons_and_masks():

    print("\n" + "=" * 60)
    print("COMPARISONS, MASKS AND BOOLEAN ARRAYS")
    print("=" * 60)

    # Products with low stock
    low_stock_mask = stock < 80

    print("\nLow Stock Mask:")
    print(low_stock_mask)

    print("\nProducts With Stock Below 80:")
    print(
        df[low_stock_mask][
            [
                "Product_ID",
                "Product_Name",
                "Stock"
            ]
        ]
    )

    # Products with high sales
    high_sales_mask = sales > 50

    print("\nHigh Sales Mask:")
    print(high_sales_mask)

    print("\nProducts With Monthly Sales Above 50:")
    print(
        df[high_sales_mask][
            [
                "Product_ID",
                "Product_Name",
                "Monthly_Sales"
            ]
        ]
    )

    # Products with high stock and low sales
    dead_stock_mask = (
        (stock > 100) &
        (sales < 30)
    )

    print("\nPotential Dead Stock:")
    print(
        df[dead_stock_mask][
            [
                "Product_ID",
                "Product_Name",
                "Stock",
                "Monthly_Sales"
            ]
        ]
    )

    # Any and all
    print("\nIs any product below 50 stock?")
    print(
        np.any(stock < 50)
    )

    print("\nAre all products above 0 stock?")
    print(
        np.all(stock > 0)
    )


# ============================================================
# 5. FANCY INDEXING
# ============================================================

def fancy_indexing():

    print("\n" + "=" * 60)
    print("FANCY INDEXING")
    print("=" * 60)

    # Select specific positions
    indexes = np.array([
        0,
        4,
        8,
        12,
        16
    ])

    selected_stock = stock[indexes]

    selected_sales = sales[indexes]

    print("\nSelected Indexes:")
    print(indexes)

    print("\nStock at Selected Indexes:")
    print(selected_stock)

    print("\nSales at Selected Indexes:")
    print(selected_sales)

    print("\nCorresponding Products:")

    print(
        df.iloc[indexes][
            [
                "Product_ID",
                "Product_Name",
                "Stock",
                "Monthly_Sales"
            ]
        ]
    )


# ============================================================
# 6. SORTING ARRAYS
# ============================================================

def sorting_arrays():

    print("\n" + "=" * 60)
    print("SORTING ARRAYS")
    print("=" * 60)

    # Sort stock
    sorted_stock = np.sort(stock)

    print("\nStock Sorted Ascending:")
    print(sorted_stock)

    # Sort sales
    sorted_sales = np.sort(sales)

    print("\nSales Sorted Ascending:")
    print(sorted_sales)

    # Get indexes that would sort the array
    sort_indexes = np.argsort(sales)

    print("\nProducts Sorted By Monthly Sales:")
    print(
        df.iloc[
            sort_indexes
        ][
            [
                "Product_ID",
                "Product_Name",
                "Monthly_Sales"
            ]
        ]
    )

    # Top 5 products
    top_indexes = np.argsort(sales)[-5:][::-1]

    print("\nTop 5 Products By Monthly Sales:")
    print(
        df.iloc[
            top_indexes
        ][
            [
                "Product_ID",
                "Product_Name",
                "Monthly_Sales"
            ]
        ]
    )


# ============================================================
# 7. DATA VISUALIZATION
# ============================================================

def visualization():

    while True:

        print("\n" + "=" * 60)
        print("DATA VISUALIZATION")
        print("=" * 60)

        print("1. Bar Chart - Stock by Product")
        print("2. Line Chart - Monthly Sales")
        print("3. Scatter Plot - Stock vs Sales")
        print("4. Pie Chart - Stock by Category")
        print("5. Histogram - Stock Distribution")
        print("6. Back")

        choice = input("\nEnter Choice: ")

        # Bar chart
        if choice == "1":

            plt.figure(figsize=(12, 6))

            plt.bar(
                df["Product_ID"],
                stock
            )

            plt.title(
                "Inventory Stock by Product"
            )

            plt.xlabel("Product ID")
            plt.ylabel("Stock Quantity")

            plt.xticks(rotation=45)

            plt.tight_layout()

            plt.show()

        # Line chart
        elif choice == "2":

            plt.figure(figsize=(12, 6))

            plt.plot(
                df["Product_ID"],
                sales,
                marker="o"
            )

            plt.title(
                "Monthly Sales by Product"
            )

            plt.xlabel("Product ID")
            plt.ylabel("Monthly Sales")

            plt.xticks(rotation=45)

            plt.grid(True)

            plt.tight_layout()

            plt.show()

        # Scatter plot
        elif choice == "3":

            plt.figure(figsize=(8, 6))

            plt.scatter(
                stock,
                sales
            )

            plt.title(
                "Stock vs Monthly Sales"
            )

            plt.xlabel("Stock Quantity")
            plt.ylabel("Monthly Sales")

            plt.grid(True)

            plt.tight_layout()

            plt.show()

        # Pie chart
        elif choice == "4":

            category_stock = (
                df.groupby("Category")["Stock"]
                .sum()
            )

            plt.figure(figsize=(8, 8))

            plt.pie(
                category_stock.values,
                labels=category_stock.index,
                autopct="%1.1f%%"
            )

            plt.title(
                "Stock Distribution by Category"
            )

            plt.show()

        # Histogram
        elif choice == "5":

            plt.figure(figsize=(8, 6))

            plt.hist(
                stock,
                bins=5
            )

            plt.title(
                "Stock Quantity Distribution"
            )

            plt.xlabel("Stock Quantity")
            plt.ylabel("Number of Products")

            plt.grid(True)

            plt.tight_layout()

            plt.show()

        elif choice == "6":

            break

        else:

            print("Invalid choice.")


# ============================================================
# 8. RUN ALL NUMPY OPERATIONS
# ============================================================

def run_all():

    numpy_computation()

    aggregations()

    array_operations()

    comparisons_and_masks()

    fancy_indexing()

    sorting_arrays()


# ============================================================
# MAIN MENU
# ============================================================

while True:

    print("\n")
    print("=" * 60)
    print("             INVENTORYIQ NUMPY ANALYSIS")
    print("=" * 60)

    print("1. Computation With NumPy")
    print("2. Aggregations")
    print("3. Computation on Arrays")
    print("4. Comparisons, Masks and Boolean Arrays")
    print("5. Fancy Indexing")
    print("6. Sorting Arrays")
    print("7. Data Visualization")
    print("8. Run All NumPy Operations")
    print("9. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        numpy_computation()

    elif choice == "2":

        aggregations()

    elif choice == "3":

        array_operations()

    elif choice == "4":

        comparisons_and_masks()

    elif choice == "5":

        fancy_indexing()

    elif choice == "6":

        sorting_arrays()

    elif choice == "7":

        visualization()

    elif choice == "8":

        run_all()

    elif choice == "9":

        print(
            "\nThank you for using InventoryIQ!"
        )

        break

    else:

        print(
            "\nInvalid choice. Please try again."
        )