from pathlib import Path

import sys
import re

from abc import ABC, abstractmethod

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QMessageBox,
    QVBoxLayout,
    QFormLayout,
    QHBoxLayout
)


# Abstract parent class
class InventoryItem(ABC):

    def __init__(self, product_id, product_name, stock_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.stock_quantity = stock_quantity

    @abstractmethod
    def calculate_risk_score(self):
        pass


# Dead stock class
class DeadStockItem(InventoryItem):

    def __init__(
        self,
        product_id,
        product_name,
        stock_quantity,
        monthly_sales
    ):
        super().__init__(
            product_id,
            product_name,
            stock_quantity
        )

        self.monthly_sales = monthly_sales

    def calculate_risk_score(self):
        return self.stock_quantity / (self.monthly_sales + 1)


# Fast moving class
class FastMovingItem(InventoryItem):

    def __init__(
        self,
        product_id,
        product_name,
        stock_quantity,
        monthly_sales
    ):
        super().__init__(
            product_id,
            product_name,
            stock_quantity
        )

        self.monthly_sales = monthly_sales

    def calculate_risk_score(self):
        return self.monthly_sales / self.stock_quantity


# Main window
class InventoryIQ(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("InventoryIQ")
        self.resize(700, 600)
        self.setMinimumSize(600, 500)

        self.create_ui()
        self.connect_signals()
        self.apply_style()


    # Create the interface
    def create_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(40, 30, 40, 30)
        main_layout.setSpacing(15)

        # Title
        title = QLabel("InventoryIQ")
        title.setObjectName("title")

        subtitle = QLabel("Inventory Analysis")
        subtitle.setObjectName("subtitle")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # Product form
        form_layout = QFormLayout()
        form_layout.setContentsMargins(0, 15, 0, 10)
        form_layout.setHorizontalSpacing(18)
        form_layout.setVerticalSpacing(12)

        self.product_id = QLineEdit()
        self.product_name = QLineEdit()
        self.stock_quantity = QLineEdit()
        self.monthly_sales = QLineEdit()

        self.product_id.setPlaceholderText("Example: P101")
        self.product_name.setPlaceholderText("Example: Nike Shoes")
        self.stock_quantity.setPlaceholderText("Example: 500")
        self.monthly_sales.setPlaceholderText("Example: 20")

        self.item_type = QComboBox()

        self.item_type.addItems([
            "Dead Stock",
            "Fast Moving"
        ])

        form_layout.addRow(
            "Product ID:",
            self.product_id
        )

        form_layout.addRow(
            "Product Name:",
            self.product_name
        )

        form_layout.addRow(
            "Stock Quantity:",
            self.stock_quantity
        )

        form_layout.addRow(
            "Monthly Sales:",
            self.monthly_sales
        )

        form_layout.addRow(
            "Item Type:",
            self.item_type
        )

        main_layout.addLayout(form_layout)

        # Buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        self.submit_button = QPushButton("Submit")
        self.clear_button = QPushButton("Clear")
        self.exit_button = QPushButton("Exit")

        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.exit_button)

        main_layout.addLayout(button_layout)

        main_layout.addStretch()


    # Connect buttons to functions
    def connect_signals(self):

        self.submit_button.clicked.connect(self.submit)
        self.clear_button.clicked.connect(self.clear)
        self.exit_button.clicked.connect(self.confirm_exit)


    # Validate and process input
    def submit(self):

        try:

            product_id = self.product_id.text().strip()
            product_name = self.product_name.text().strip()
            stock_text = self.stock_quantity.text().strip()
            sales_text = self.monthly_sales.text().strip()
            item_type = self.item_type.currentText()

            # Check empty fields
            if not product_id:
                raise ValueError("Product ID cannot be empty.")

            if not product_name:
                raise ValueError("Product Name cannot be empty.")

            if not stock_text:
                raise ValueError("Stock Quantity cannot be empty.")

            if not sales_text:
                raise ValueError("Monthly Sales cannot be empty.")

            # Validate product ID
            if not re.fullmatch(r"P\\d+", product_id):
                raise ValueError("Product ID must be like P101.")

            # Validate product name
            if not re.fullmatch(r"[A-Za-z ]+", product_name):
                raise ValueError(
                    "Product Name should contain only letters."
                )

            # Convert numbers
            stock = int(stock_text)
            sales = int(sales_text)

            # Validate numbers
            if stock <= 0:
                raise ValueError(
                    "Stock Quantity must be greater than 0."
                )

            if sales < 0:
                raise ValueError(
                    "Monthly Sales cannot be negative."
                )

            # Create the correct object
            if item_type == "Dead Stock":
                item = DeadStockItem(
                    product_id,
                    product_name,
                    stock,
                    sales
                )
            else:
                item = FastMovingItem(
                    product_id,
                    product_name,
                    stock,
                    sales
                )

            # Calculate result
            score = item.calculate_risk_score()

            # Display result
            QMessageBox.information(
                self,
                "Validation Successful",
                f"Product ID: {product_id}\\n"
                f"Product Name: {product_name}\\n"
                f"Stock Quantity: {stock}\\n"
                f"Monthly Sales: {sales}\\n"
                f"Item Type: {item_type}\\n"
                f"Score: {score:.2f}"
            )

        except ValueError as error:

            QMessageBox.warning(
                self,
                "Invalid Input",
                str(error)
            )

        except Exception as error:

            QMessageBox.critical(
                self,
                "Error",
                f"An unexpected error occurred:\\n{error}"
            )


    # Clear all inputs
    def clear(self):

        self.product_id.clear()
        self.product_name.clear()
        self.stock_quantity.clear()
        self.monthly_sales.clear()

        self.item_type.setCurrentIndex(0)
        self.product_id.setFocus()


    # Confirm before closing
    def confirm_exit(self):

        result = QMessageBox.question(
            self,
            "Exit",
            "Are you sure you want to exit?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )

        if result == QMessageBox.StandardButton.Yes:
            self.close()


    # Apply application styling
    def apply_style(self):

        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
            }

            QLabel {
                color: #EAEAEA;
                font-size: 14px;
            }

            #title {
                color: #7C6CFF;
                font-size: 34px;
                font-weight: bold;
            }

            #subtitle {
                color: #999999;
                font-size: 15px;
            }

            QFormLayout QLabel {
                color: #DCDCDC;
                font-size: 14px;
                font-weight: 500;
            }

            QLineEdit {
                background-color: #1E1E1E;
                color: #FFFFFF;
                border: 1px solid #383838;
                border-radius: 7px;
                padding: 9px 12px;
                font-size: 14px;
                min-height: 22px;
            }

            QLineEdit:focus {
                border: 1px solid #5B4BFF;
            }

            QLineEdit::placeholder {
                color: #777777;
            }

            QComboBox {
                background-color: #1E1E1E;
                color: #FFFFFF;
                border: 1px solid #383838;
                border-radius: 7px;
                padding: 9px 12px;
                font-size: 14px;
                min-height: 22px;
            }

            QComboBox:hover {
                border: 1px solid #5B4BFF;
            }

            QComboBox:focus {
                border: 1px solid #5B4BFF;
            }

            QComboBox QAbstractItemView {
                background-color: #1E1E1E;
                color: #FFFFFF;
                border: 1px solid #383838;
                selection-background-color: #5B4BFF;
                selection-color: #FFFFFF;
                padding: 5px;
            }

            QPushButton {
                background-color: #5B4BFF;
                color: #FFFFFF;
                border: none;
                border-radius: 7px;
                min-height: 42px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #6C5CFF;
            }

            QPushButton:pressed {
                background-color: #4939E8;
            }
        """)


# Start application
app = QApplication(sys.argv)

window = InventoryIQ()
window.show()

sys.exit(app.exec())

out = Path("/mnt/data/inventoryiq_fixed.py")
out.write_text(fixed_code, encoding="utf-8")
print(f"Fixed file created: {out}")
