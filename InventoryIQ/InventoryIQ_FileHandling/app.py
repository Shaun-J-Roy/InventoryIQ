import streamlit as st
import re
import os
import shutil


# File names
DATA_FILE = "inventory.txt"
BACKUP_FILE = "inventory_backup.txt"


# Create the inventory file
def create_file():

    try:
        with open(DATA_FILE, "w") as file:
            file.write("")

        return True

    except OSError:
        return False


# Read all records
def read_records():

    try:

        with open(DATA_FILE, "r") as file:

            # Demonstrate read()
            content = file.read()

            # Demonstrate tell()
            position = file.tell()

            # Move back to beginning
            file.seek(0)

            # Demonstrate readlines()
            lines = file.readlines()

            file.close()

        records = []

        for line in lines:

            line = line.strip()

            if line:

                fields = line.split("|")

                if len(fields) == 6:

                    records.append({
                        "Product ID": fields[0],
                        "Product Name": fields[1],
                        "Category": fields[2],
                        "Stock Quantity": fields[3],
                        "Monthly Sales": fields[4],
                        "Supplier Email": fields[5]
                    })

        return records

    except FileNotFoundError:

        return []


# Read the first record
def read_first_line():

    try:

        with open(DATA_FILE, "r") as file:

            # Demonstrate readline()
            first_line = file.readline()

            file.close()

        return first_line.strip()

    except FileNotFoundError:

        return ""


# Add a new record
def append_record(record):

    try:

        with open(DATA_FILE, "a") as file:

            line = (
                record["Product ID"] + "|" +
                record["Product Name"] + "|" +
                record["Category"] + "|" +
                record["Stock Quantity"] + "|" +
                record["Monthly Sales"] + "|" +
                record["Supplier Email"] + "\n"
            )

            # Demonstrate write()
            file.write(line)

            file.close()

        return True

    except OSError:

        return False

# Demonstrate r+ file mode
def demonstrate_rplus():

    try:
        with open(DATA_FILE, "r+") as file:

            # Get current file position
            start_position = file.tell()

            # Read the complete file
            content = file.read()

            # Move the pointer back to the beginning
            file.seek(0)

            # Rewrite the same content
            file.write(content)

            # Close the file
            file.close()

        return start_position

    except FileNotFoundError:
        return None

    except OSError:
        return None


# Search for a product
def search_record(product_id):

    records = read_records()

    for record in records:

        if record["Product ID"].lower() == product_id.lower():

            return record

    return None


# Update a product
def update_record(product_id, updated_record):

    try:

        records = read_records()

        found = False

        for index, record in enumerate(records):

            if record["Product ID"].lower() == product_id.lower():

                records[index] = updated_record

                found = True

                break

        if not found:
            return False

        lines = []

        for record in records:

            line = (
                record["Product ID"] + "|" +
                record["Product Name"] + "|" +
                record["Category"] + "|" +
                record["Stock Quantity"] + "|" +
                record["Monthly Sales"] + "|" +
                record["Supplier Email"] + "\n"
            )

            lines.append(line)

        # Demonstrate w+ and writelines()
        with open(DATA_FILE, "w+") as file:

            file.writelines(lines)

            file.seek(0)

            file.close()

        return True

    except OSError:

        return False


# Delete a product
def delete_record(product_id):

    try:

        records = read_records()

        new_records = []

        found = False

        for record in records:

            if record["Product ID"].lower() == product_id.lower():

                found = True

            else:

                new_records.append(record)

        if not found:
            return False

        lines = []

        for record in new_records:

            line = (
                record["Product ID"] + "|" +
                record["Product Name"] + "|" +
                record["Category"] + "|" +
                record["Stock Quantity"] + "|" +
                record["Monthly Sales"] + "|" +
                record["Supplier Email"] + "\n"
            )

            lines.append(line)

        with open(DATA_FILE, "w") as file:

            file.writelines(lines)

            file.close()

        return True

    except OSError:

        return False


# Create backup
def create_backup():

    try:

        if not os.path.exists(DATA_FILE):

            return False

        shutil.copy(
            DATA_FILE,
            BACKUP_FILE
        )

        return True

    except OSError:

        return False


# Validate product ID
def validate_product_id(product_id):

    return bool(
        re.fullmatch(
            r"P\d{3}",
            product_id
        )
    )


# Validate product name
def validate_product_name(name):

    return bool(
        re.fullmatch(
            r"[A-Za-z ]+",
            name
        )
    )


# Validate email
def validate_email(email):

    return bool(
        re.fullmatch(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            email
        )
    )


# Validate a record
def validate_record(
    product_id,
    product_name,
    category,
    stock,
    sales,
    email
):

    if not validate_product_id(product_id):

        return "Product ID must be in the format P101."

    if not validate_product_name(product_name):

        return "Product Name should contain only letters."

    if not category:

        return "Please select a category."

    if stock < 0:

        return "Stock Quantity cannot be negative."

    if sales < 0:

        return "Monthly Sales cannot be negative."

    if not validate_email(email):

        return "Please enter a valid supplier email."

    return None


# Page configuration
st.set_page_config(
    page_title="InventoryIQ File Manager",
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
    font-size: 38px;
    font-weight: bold;
}

.subtitle {
    color: #999999;
    font-size: 16px;
}

div.stButton > button {
    background-color: #5B4BFF;
    color: white;
    border: none;
    border-radius: 7px;
}

div.stButton > button:hover {
    background-color: #6C5CFF;
}

</style>
""", unsafe_allow_html=True)


# Page header
st.markdown(
    '<div class="title">InventoryIQ</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'File-Based Inventory Management'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# Sidebar
st.sidebar.title("InventoryIQ")

operation = st.sidebar.radio(
    "Select Operation",
    [
        "Create File",
        "View Records",
        "Add Record",
        "Search Record",
        "Update Record",
        "Delete Record",
        "Create Backup"
    ]
)


# Create file
if operation == "Create File":

    st.header("Create Inventory File")

    st.write(
        "Create or reset the inventory text file."
    )

    if st.button("Create File"):

        if create_file():

            st.success(
                "Inventory file created successfully."
            )

        else:

            st.error(
                "Unable to create the inventory file."
            )


# View records
elif operation == "View Records":

    st.header("Inventory Records")

    records = read_records()

    if records:

        st.dataframe(
            records,
            use_container_width=True,
            hide_index=True
        )

        st.info(
            f"Total records: {len(records)}"
        )

        first_line = read_first_line()

        if first_line:

            with st.expander(
                "File Handling Demonstration"
            ):

                st.write(
                    "First line using readline():"
                )

                st.code(first_line)

                st.write(
                    "The application also uses "
                    "read(), readlines(), seek(), "
                    "tell(), and close()."
                )

    else:

        st.warning(
            "No records found. Create the file "
            "and add some records."
        )


# Add record
elif operation == "Add Record":

    st.header("Add Inventory Record")

    with st.form("add_form"):

        product_id = st.text_input(
            "Product ID",
            placeholder="P111"
        )

        product_name = st.text_input(
            "Product Name",
            placeholder="Nike Shoes"
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

        sales = st.number_input(
            "Monthly Sales",
            min_value=0,
            step=1
        )

        email = st.text_input(
            "Supplier Email",
            placeholder="supplier@example.com"
        )

        submitted = st.form_submit_button(
            "Add Record"
        )

    if submitted:

        error = validate_record(
            product_id,
            product_name,
            category,
            stock,
            sales,
            email
        )

        if error:

            st.error(error)

        elif search_record(product_id):

            st.warning(
                "A product with this ID already exists."
            )

        else:

            record = {
                "Product ID": product_id,
                "Product Name": product_name,
                "Category": category,
                "Stock Quantity": str(stock),
                "Monthly Sales": str(sales),
                "Supplier Email": email
            }

            if append_record(record):

                st.success(
                    "Product added successfully."
                )

            else:

                st.error(
                    "Unable to save the record."
                )


# Search record
elif operation == "Search Record":

    st.header("Search Inventory")

    product_id = st.text_input(
        "Enter Product ID",
        placeholder="P101"
    )

    if st.button("Search"):

        if not validate_product_id(product_id):

            st.error(
                "Enter a valid Product ID such as P101."
            )

        else:

            record = search_record(product_id)

            if record:

                st.success(
                    "Product found."
                )

                st.json(record)

            else:

                st.warning(
                    "Product not found."
                )


# Update record
elif operation == "Update Record":

    st.header("Update Inventory Record")

    product_id = st.text_input(
        "Product ID to Update",
        placeholder="P101"
    )

    if st.button("Load Product"):

        record = search_record(product_id)

        if record:

            st.session_state["update_record"] = record

            st.success(
                "Product loaded."
            )

        else:

            st.warning(
                "Product not found."
            )

    if "update_record" in st.session_state:

        record = st.session_state["update_record"]

        with st.form("update_form"):

            new_name = st.text_input(
                "Product Name",
                value=record["Product Name"]
            )

            new_category = st.selectbox(
                "Category",
                [
                    "Clothing",
                    "Footwear",
                    "Electronics",
                    "Accessories"
                ],
                index=[
                    "Clothing",
                    "Footwear",
                    "Electronics",
                    "Accessories"
                ].index(record["Category"])
            )

            new_stock = st.number_input(
                "Stock Quantity",
                min_value=0,
                value=int(record["Stock Quantity"]),
                step=1
            )

            new_sales = st.number_input(
                "Monthly Sales",
                min_value=0,
                value=int(record["Monthly Sales"]),
                step=1
            )

            new_email = st.text_input(
                "Supplier Email",
                value=record["Supplier Email"]
            )

            update_button = st.form_submit_button(
                "Update Record"
            )

        if update_button:

            error = validate_record(
                product_id,
                new_name,
                new_category,
                new_stock,
                new_sales,
                new_email
            )

            if error:

                st.error(error)

            else:

                updated_record = {
                    "Product ID": product_id,
                    "Product Name": new_name,
                    "Category": new_category,
                    "Stock Quantity": str(new_stock),
                    "Monthly Sales": str(new_sales),
                    "Supplier Email": new_email
                }

                if update_record(
                    product_id,
                    updated_record
                ):

                    st.success(
                        "Product updated successfully."
                    )

                    del st.session_state[
                        "update_record"
                    ]

                else:

                    st.error(
                        "Unable to update the product."
                    )


# Delete record
elif operation == "Delete Record":

    st.header("Delete Inventory Record")

    product_id = st.text_input(
        "Product ID to Delete",
        placeholder="P101"
    )

    if st.button("Delete Product"):

        if not validate_product_id(product_id):

            st.error(
                "Enter a valid Product ID."
            )

        elif delete_record(product_id):

            st.success(
                "Product deleted successfully."
            )

        else:

            st.warning(
                "Product not found."
            )


# Create backup
elif operation == "Create Backup":

    st.header("Backup Inventory Data")

    st.write(
        "Create a backup copy of the inventory file."
    )

    if st.button("Create Backup"):

        if create_backup():

            st.success(
                "Backup created successfully."
            )

        else:

            st.error(
                "Unable to create backup."
            )
