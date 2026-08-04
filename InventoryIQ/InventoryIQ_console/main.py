from abc import ABC, abstractmethod


# Abstract Class
class InventoryItem(ABC):
    def __init__(self, product_id, product_name, stock_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.stock_quantity = stock_quantity

    def display_info(self):
        print(f"\nProduct ID      : {self.product_id}")
        print(f"Product Name    : {self.product_name}")
        print(f"Stock Quantity  : {self.stock_quantity}")

    @abstractmethod
    def calculate_risk_score(self):
        pass


# Derived Class 1
class DeadStockItem(InventoryItem):
    def __init__(self, product_id, product_name, stock_quantity, monthly_sales):
        super().__init__(product_id, product_name, stock_quantity)
        self.monthly_sales = monthly_sales

    def calculate_risk_score(self):
        risk_score = self.stock_quantity / (self.monthly_sales + 1)

        self.display_info()
        print(f"Monthly Sales   : {self.monthly_sales}")
        print(f"Risk Score      : {risk_score:.2f}")
        print("Status          : Dead Stock")


# Derived Class 2
class FastMovingItem(InventoryItem):
    def __init__(self, product_id, product_name, stock_quantity, monthly_sales):
        super().__init__(product_id, product_name, stock_quantity)
        self.monthly_sales = monthly_sales

    def calculate_risk_score(self):
        performance_score = self.monthly_sales / self.stock_quantity

        self.display_info()
        print(f"Monthly Sales   : {self.monthly_sales}")
        print(f"Performance Score : {performance_score:.2f}")
        print("Status            : Fast Moving")


# Main Program
inventory = []


def start_inventory():

    global inventory

    while True:

        print("\n==============================")
        print("      InventoryIQ")
        print("==============================")
        print("1. Add Dead Stock Item")
        print("2. Add Fast Moving Item")
        print("3. Display Inventory Analysis")
        print("4. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            try:

                product_id = input("Enter Product ID: ")
                product_name = input("Enter Product Name: ")
                stock_quantity = int(input("Enter Stock Quantity: "))
                monthly_sales = int(input("Enter Monthly Sales: "))

                item = DeadStockItem(
                    product_id,
                    product_name,
                    stock_quantity,
                    monthly_sales
                )

                inventory.append(item)

                print("\nDead Stock Item Added Successfully!")

            except ValueError:
                print("Please enter valid numeric values.")

        elif choice == "2":

            try:

                product_id = input("Enter Product ID: ")
                product_name = input("Enter Product Name: ")
                stock_quantity = int(input("Enter Stock Quantity: "))
                monthly_sales = int(input("Enter Monthly Sales: "))

                item = FastMovingItem(
                    product_id,
                    product_name,
                    stock_quantity,
                    monthly_sales
                )

                inventory.append(item)

                print("\nFast Moving Item Added Successfully!")

            except ValueError:
                print("Please enter valid numeric values.")

        elif choice == "3":

            if len(inventory) == 0:

                print("\nNo products available!")

            else:

                print("\n===== Inventory Analysis =====")

                for item in inventory:

                    item.calculate_risk_score()

        elif choice == "4":

            print("\nLogging out...\n")

            break

        else:

            print("Invalid Choice! Please try again.")

if __name__ == "__main__":
    start_inventory()