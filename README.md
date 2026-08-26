# InventoryIQ

InventoryIQ is my Python-based inventory management project developed across my laboratory programs.

I chose **Inventory Management** as the common domain so I could apply different Python concepts to a consistent real-world problem.

## Project Structure

```text
InventoryIQ/
│
├── InventoryIQ/
│   ├── InventoryIQ_API/
│   │   ├── client.py
│   │   ├── inventory.json
│   │   └── server.py
│   │
│   ├── InventoryIQ_console/
│   │   ├── login.py
│   │   ├── main.py
│   │   └── users.json
│   │
│   ├── InventoryIQ_FileHandling/
│   │   ├── app.py
│   │   ├── inventory.txt
│   │   ├── inventory_backup.txt
│   │   └── requirements.txt
│   │
│   ├── InventoryIQ_GUI/
│   │   ├── api.py
│   │   ├── inventoryiq.py
│   │   ├── products.json
│   │   ├── requirements.txt
│   │   └── users.json
│   │
│   ├── InventoryIQ_NumPy/
│   │   ├── inventory_numpy.csv
│   │   ├── numpy_lab.py
│   │   └── requirements.txt
│   │
│   ├── InventoryIQ_Streamlit/
│   │   ├── app.py
│   │   ├── inventory.json
│   │   └── requirements.txt
│   │
│   └── Pandas_Lab/
│       ├── pandas_lab.py
│       └── web_server_log_100_records.csv
```

---

## P1 - Object-Oriented Programming

**Location:** `InventoryIQ_console/`

**Main file:** `main.py`

### Run

```bash
cd InventoryIQ/InventoryIQ_console
python main.py
```

This program demonstrates:

* Classes and objects
* Inheritance
* Abstract classes
* Abstract methods
* Hierarchical inheritance
* Polymorphism

`InventoryItem` is the abstract parent class, with `DeadStockItem` and `FastMovingItem` as derived classes.

---

## P2 - Regular Expression Login and Registration

**Location:** `InventoryIQ_console/`

**Main file:** `login.py`

### Run

```bash
cd InventoryIQ/InventoryIQ_console
python login.py
```

This program implements user registration and login using JSON storage, regular expressions, and exception handling.

It demonstrates the required regex functions:

* `search()`
* `match()`
* `fullmatch()`
* `findall()`
* `split()`
* `compile()`
* `sub()`

The registration process validates the user's name, email, phone number, and password.

---

## P3 - PyQt6 GUI

**Location:** `InventoryIQ_GUI/`

**Main file:** `inventoryiq.py`

### Run

```bash
cd InventoryIQ/InventoryIQ_GUI
python inventoryiq.py
```

This is the PyQt6 version of InventoryIQ.

It accepts product information, validates the input, creates the appropriate inventory object, calculates the result, and displays it using dialog boxes.

The GUI also contains the P4 public API functionality through `api.py`.

---

## P4 - Public API and JSON Processing

**Location:** `InventoryIQ_GUI/`

**Main file:** `api.py`

This program fetches product information from a public API and processes the returned JSON data.

It uses dictionary operations to extract and process values from the API response.

The API functionality is also connected to the PyQt6 GUI through `inventoryiq.py`.

### Run directly

```bash
cd InventoryIQ/InventoryIQ_GUI
python api.py
```

---

## P5 - Flask Web API

**Location:** `InventoryIQ_API/`

**Files:**

```text
server.py
client.py
inventory.json
```

### Start the server

```bash
cd InventoryIQ/InventoryIQ_API
python server.py
```

Keep the server running.

### Run the client

Open another terminal:

```bash
cd InventoryIQ/InventoryIQ_API
python client.py
```

The API supports:

* GET
* POST
* PUT
* DELETE
* JSON data exchange
* HTTP status codes
* Error handling

The Flask server provides endpoints for retrieving, adding, updating, and deleting inventory products.

---

## P6 - Streamlit Application

**Location:** `InventoryIQ_Streamlit/`

**Main file:** `app.py`

### Run

```bash
cd InventoryIQ/InventoryIQ_Streamlit
python -m streamlit run app.py
```

The application provides:

* Dashboard
* Inventory table
* Category filtering
* Add Product form
* Inventory analytics
* Data visualizations

The application uses `inventory.json` as its sample dataset.

---

## P7 - File Handling

**Location:** `InventoryIQ_FileHandling/`

**Main file:** `app.py`

### Run

```bash
cd InventoryIQ/InventoryIQ_FileHandling
python -m streamlit run app.py
```

This application manages inventory records using a text file.

It demonstrates:

* Create
* Read
* Append
* Search
* Update
* Delete
* Backup

It also demonstrates file modes such as:

* `w`
* `r`
* `a`
* `r+`
* `w+`

and file handling methods such as:

* `read()`
* `readline()`
* `readlines()`
* `write()`
* `writelines()`
* `seek()`
* `tell()`
* `close()`

---

## P8 - Pandas

**Location:** `Pandas_Lab/`

**Main file:** `pandas_lab.py`

**Dataset:** `web_server_log_100_records.csv`

### Run

```bash
cd InventoryIQ/Pandas_Lab
python pandas_lab.py
```

This program performs Pandas operations on the web server log dataset.

It covers:

* Data loading
* `head()` and `tail()`
* Dataset information
* Descriptive statistics
* Missing values
* Unique values
* Indexing
* `loc[]`
* `iloc[]`
* Conditional filtering
* IP address analysis

---

## P9 - NumPy

**Location:** `InventoryIQ_NumPy/`

**Main file:** `numpy_lab.py`

**Dataset:** `inventory_numpy.csv`

### Run

```bash
cd InventoryIQ/InventoryIQ_NumPy
python numpy_lab.py
```

This program performs NumPy operations on inventory data.

It covers:

* Computation with NumPy
* Aggregations
* Array operations
* Comparisons
* Boolean arrays
* Masks
* Fancy indexing
* Sorting
* Data visualization

The visualization section includes:

* Bar charts
* Line charts
* Scatter plots
* Pie charts
* Histograms

---

## Technologies Used

* Python
* PyQt6
* Flask
* Streamlit
* Requests
* Pandas
* NumPy
* Matplotlib
* JSON
* Regular Expressions

---

## Running the Project

Each laboratory is kept in a separate folder so that the programs can be run independently.

For normal Python programs:

```bash
python filename.py
```

For Streamlit programs:

```bash
python -m streamlit run app.py
```

For the Flask API:

```bash
python server.py
```

Then run the client in a separate terminal:

```bash
python client.py
```

---

## Notes

The Inventory Management domain is reused across the programs wherever appropriate, while the Pandas laboratory uses the web server log dataset specified for that exercise.
