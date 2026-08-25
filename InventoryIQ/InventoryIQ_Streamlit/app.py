import json
import streamlit as st
import pandas as pd


# Load inventory data
def load_data():

    try:
        with open("inventory.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Save inventory data
def save_data(products):

    with open("inventory.json", "w") as file:
        json.dump(products, file, indent=4)


# Page settings
st.set_page_config(
    page_title="InventoryIQ",
    page_icon="📦",
    layout="wide"
)


# Dark theme
st.markdown("""
<style>

    .stApp {
        background-color: #121212;
        color: #EAEAEA;
    }

    [data-testid="stSidebar"] {
        background-color: #1A1A1A;
    }

    .title {
        color: #7C6CFF;
        font-size: 40px;
        font-weight: bold;
    }

    .subtitle {
        color: #999999;
        font-size: 16px;
    }

    .metric-card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }

</style>
""", unsafe_allow_html=True)


# Load products
products = load_data()

# Sidebar
st.sidebar.title("InventoryIQ")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Inventory",
        "Add Product",
        "Analytics"
    ]
)


# Dashboard
if page == "Dashboard":

    st.markdown(
        '<div class="title">InventoryIQ</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Smart Inventory Analytics and Dead Stock Management'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    total_products = len(products)

    total_stock = sum(
        product.get("stock", 0)
        for product in products
    )

    total_sales = sum(
        product.get("monthly_sales", 0)
        for product in products
    )

    dead_stock = sum(
        1
        for product in products
        if product.get("monthly_sales", 0) < 20
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Products",
        total_products
    )

    col2.metric(
        "Total Stock",
        total_stock
    )

    col3.metric(
        "Monthly Sales",
        total_sales
    )

    col4.metric(
        "Dead Stock",
        dead_stock
    )

    st.subheader("Inventory Overview")

    if products:

        df = pd.DataFrame(products)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No inventory data available.")


# Inventory page
elif page == "Inventory":

    st.title("Inventory")

    if products:

        df = pd.DataFrame(products)

        # Category filter
        categories = sorted(
            df["category"].unique()
        )

        selected_category = st.selectbox(
            "Filter by Category",
            ["All"] + categories
        )

        if selected_category != "All":

            df = df[
                df["category"] == selected_category
            ]

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.write(
            f"Showing {len(df)} product(s)"
        )

    else:

        st.info("No products available.")


# Add product page
elif page == "Add Product":

    st.title("Add Product")

    st.write(
        "Enter the details of a new inventory item."
    )

    with st.form("product_form"):

        product_id = st.text_input(
            "Product ID",
            placeholder="Example: P111"
        )

        product_name = st.text_input(
            "Product Name",
            placeholder="Example: Puma Jacket"
        )

        category = st.selectbox(
            "Category",
            [
                "Clothing",
                "Footwear",
                "Electronics",
                "Accessories"
            ]
        )

        stock = st.number_input(
            "Stock Quantity",
            min_value=0,
            step=1
        )

        monthly_sales = st.number_input(
            "Monthly Sales",
            min_value=0,
            step=1
        )

        submitted = st.form_submit_button(
            "Add Product"
        )

    if submitted:

        if not product_id or not product_name:

            st.error(
                "Product ID and Product Name are required."
            )

        elif any(
            product["product_id"] == product_id
            for product in products
        ):

            st.error(
                "Product ID already exists."
            )

        else:

            new_product = {
                "product_id": product_id,
                "product_name": product_name,
                "category": category,
                "stock": stock,
                "monthly_sales": monthly_sales
            }

            products.append(new_product)

            save_data(products)

            st.success(
                f"{product_name} added successfully!"
            )


# Analytics page
elif page == "Analytics":

    st.title("Inventory Analytics")

    if products:

        df = pd.DataFrame(products)

        st.subheader("Stock by Category")

        stock_by_category = (
            df.groupby("category")["stock"]
            .sum()
        )

        st.bar_chart(
            stock_by_category
        )

        st.subheader("Monthly Sales by Category")

        sales_by_category = (
            df.groupby("category")["monthly_sales"]
            .sum()
        )

        st.bar_chart(
            sales_by_category
        )

        st.subheader("Stock vs Monthly Sales")

        chart_data = df[
            [
                "product_name",
                "stock",
                "monthly_sales"
            ]
        ].set_index("product_name")

        st.line_chart(
            chart_data
        )

    else:

        st.info(
            "No data available for analysis."
        )