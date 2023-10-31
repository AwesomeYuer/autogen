# filename: analyze_sales.py

import pandas as pd

# Read the orders data file
orders = pd.read_csv("/path/to/SamplesData/Orders.csv")

# Calculate the total sales for each product
product_sales = orders.groupby("product")["quantity"].sum()

# Print the total sales for each product
print(product_sales)