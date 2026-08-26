import pandas as pd


# Load dataset
file_path = "web_server_log_100_records.csv"

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("Error: CSV file not found.")
    exit()


# Part A
def display_dataset():

    while True:

        print("\n" + "=" * 50)
        print("LOAD AND DISPLAY DATASET")
        print("=" * 50)

        print("1. First 10 records")
        print("2. Last 10 records")
        print("3. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":

            print("\nFirst 10 Records:")
            print(df.head(10))

        elif choice == "2":

            print("\nLast 10 Records:")
            print(df.tail(10))

        elif choice == "3":

            break

        else:

            print("Invalid choice.")


# Part B
def view_data():

    while True:

        print("\n" + "=" * 50)
        print("VIEW DATA")
        print("=" * 50)

        print("1. Dataset shape")
        print("2. Column names")
        print("3. Data types")
        print("4. Dataset information")
        print("5. Descriptive statistics")
        print("6. First 5 rows")
        print("7. Last 5 rows")
        print("8. Random sample of 8")
        print("9. Missing values")
        print("10. Number of unique values")
        print("11. Unique browsers")
        print("12. HTTP status code frequency")
        print("13. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":

            print("\nShape:")
            print(df.shape)

        elif choice == "2":

            print("\nColumn Names:")
            print(df.columns.tolist())

        elif choice == "3":

            print("\nData Types:")
            print(df.dtypes)

        elif choice == "4":

            print("\nDataset Information:")
            df.info()

        elif choice == "5":

            print("\nDescriptive Statistics:")
            print(df.describe())

        elif choice == "6":

            print("\nFirst 5 Rows:")
            print(df.head(5))

        elif choice == "7":

            print("\nLast 5 Rows:")
            print(df.tail(5))

        elif choice == "8":

            print("\nRandom Sample:")
            print(df.sample(8))

        elif choice == "9":

            print("\nMissing Values:")
            print(df.isnull().sum())

        elif choice == "10":

            print("\nUnique Values:")
            print(df.nunique())

        elif choice == "11":

            print("\nUnique Browsers:")
            print(df["Browser"].unique())

        elif choice == "12":

            print("\nHTTP Status Code Frequency:")
            print(df["Status_Code"].value_counts())

        elif choice == "13":

            break

        else:

            print("Invalid choice.")


# Part C: Basic indexing
def basic_indexing():

    while True:

        print("\n" + "=" * 50)
        print("BASIC INDEXING")
        print("=" * 50)

        print("1. Display Browser column")
        print("2. Display IP_Address and Status_Code")
        print("3. First 10 rows using slicing")
        print("4. Rows 20 to 30 using iloc")
        print("5. Rows 5 to 15 with Method, URL, Status_Code")
        print("6. Record at index 25")
        print("7. Records from index 40 to 50")
        print("8. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":

            print(df["Browser"])

        elif choice == "2":

            print(
                df[
                    ["IP_Address", "Status_Code"]
                ]
            )

        elif choice == "3":

            print(df[:10])

        elif choice == "4":

            print(df.iloc[20:31])

        elif choice == "5":

            print(
                df.iloc[
                    5:16,
                    [
                        df.columns.get_loc("Method"),
                        df.columns.get_loc("URL"),
                        df.columns.get_loc("Status_Code")
                    ]
                ]
            )

        elif choice == "6":

            print(df.loc[25])

        elif choice == "7":

            print(df.loc[40:50])

        elif choice == "8":

            break

        else:

            print("Invalid choice.")


# Conditional filtering
def filtering():

    while True:

        print("\n" + "=" * 50)
        print("CONDITIONAL FILTERING")
        print("=" * 50)

        print("1. Browser is Chrome")
        print("2. Status Code is 404")
        print("3. Method is POST")
        print("4. Response Time > 500 ms")
        print("5. Status Code is 200")
        print("6. Firefox and GET")
        print("7. Status Code is 404 or 500")
        print("8. URL contains 'products'")
        print("9. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":

            print(
                df[
                    df["Browser"] == "Chrome"
                ]
            )

        elif choice == "2":

            print(
                df[
                    df["Status_Code"] == 404
                ]
            )

        elif choice == "3":

            print(
                df[
                    df["Method"] == "POST"
                ]
            )

        elif choice == "4":

            print(
                df[
                    df["Response_Time_ms"] > 500
                ]
            )

        elif choice == "5":

            print(
                df.loc[
                    df["Status_Code"] == 200,
                    ["URL", "Response_Time_ms"]
                ]
            )

        elif choice == "6":

            print(
                df[
                    (df["Browser"] == "Firefox") &
                    (df["Method"] == "GET")
                ]
            )

        elif choice == "7":

            print(
                df[
                    df["Status_Code"].isin(
                        [404, 500]
                    )
                ]
            )

        elif choice == "8":

            print(
                df[
                    df["URL"].str.contains(
                        "products",
                        case=False,
                        na=False
                    )
                ]
            )

        elif choice == "9":

            break

        else:

            print("Invalid choice.")


# Advanced indexing
def advanced_indexing():

    while True:

        print("\n" + "=" * 50)
        print("ADVANCED INDEXING")
        print("=" * 50)

        print("1. Last 15 records")
        print("2. Every 5th record")
        print("3. First 20 records with selected columns")
        print("4. Specific index numbers")
        print("5. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":

            print(
                df.iloc[-15:]
            )

        elif choice == "2":

            print(
                df.iloc[::5]
            )

        elif choice == "3":

            print(
                df.loc[
                    :19,
                    [
                        "IP_Address",
                        "Method",
                        "Browser"
                    ]
                ]
            )

        elif choice == "4":

            print(
                df.loc[
                    [5, 15, 25, 35, 45]
                ]
            )

        elif choice == "5":

            break

        else:

            print("Invalid choice.")


# IP analysis
def ip_analysis():

    print("\n" + "=" * 50)
    print("IP ADDRESS ANALYSIS")
    print("=" * 50)

    ip = input(
        "Enter IP address: "
    )

    indexed_df = df.set_index(
        "IP_Address"
    )

    try:

        result = indexed_df.loc[ip]

        print("\nRecords for", ip)
        print(result)

    except KeyError:

        print(
            "\nNo records found for this IP address."
        )


# Run all
def run_all():

    print("\n" + "=" * 60)
    print("RUNNING ALL PANDAS OPERATIONS")
    print("=" * 60)

    print("\n--- First 10 Records ---")
    print(df.head(10))

    print("\n--- Last 10 Records ---")
    print(df.tail(10))

    print("\n--- Shape ---")
    print(df.shape)

    print("\n--- Columns ---")
    print(df.columns)

    print("\n--- Data Types ---")
    print(df.dtypes)

    print("\n--- Descriptive Statistics ---")
    print(df.describe())

    print("\n--- Random Sample ---")
    print(df.sample(8))

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    print("\n--- Unique Values ---")
    print(df.nunique())

    print("\n--- Browsers ---")
    print(df["Browser"].unique())

    print("\n--- Status Code Frequency ---")
    print(df["Status_Code"].value_counts())

    print("\n--- Chrome Records ---")
    print(
        df[
            df["Browser"] == "Chrome"
        ]
    )

    print("\n--- 404 Records ---")
    print(
        df[
            df["Status_Code"] == 404
        ]
    )

    print("\n--- POST Records ---")
    print(
        df[
            df["Method"] == "POST"
        ]
    )

    print("\n--- Response Time > 500 ---")
    print(
        df[
            df["Response_Time_ms"] > 500
        ]
    )

    print("\n--- Firefox + GET ---")
    print(
        df[
            (df["Browser"] == "Firefox") &
            (df["Method"] == "GET")
        ]
    )

    print("\n--- Status 404 or 500 ---")
    print(
        df[
            df["Status_Code"].isin(
                [404, 500]
            )
        ]
    )

    print("\n--- Last 15 Records ---")
    print(df.iloc[-15:])

    print("\n--- Every 5th Record ---")
    print(df.iloc[::5])

    print("\n--- URLs containing products ---")
    print(
        df[
            df["URL"].str.contains(
                "products",
                case=False,
                na=False
            )
        ]
    )

    print("\nAll operations completed.")


# Main menu
while True:

    print("\n")
    print("=" * 50)
    print("       WEB SERVER LOG ANALYSIS")
    print("=" * 50)

    print("1. Load and Display Dataset")
    print("2. View Dataset Information")
    print("3. Basic Indexing")
    print("4. Conditional Filtering")
    print("5. Advanced Indexing")
    print("6. IP Address Analysis")
    print("7. Run All Operations")
    print("8. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        display_dataset()

    elif choice == "2":

        view_data()

    elif choice == "3":

        basic_indexing()

    elif choice == "4":

        filtering()

    elif choice == "5":

        advanced_indexing()

    elif choice == "6":

        ip_analysis()

    elif choice == "7":

        run_all()

    elif choice == "8":

        print(
            "\nThank you for using "
            "Web Server Log Analysis!"
        )

        break

    else:

        print(
            "\nInvalid choice. Please try again."
        )