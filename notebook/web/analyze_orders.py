# filename: analyze_orders.py

import pandas as pd
import requests

# Step 1: Download the orders data file
url = "http://172.23.240.251:3000/Orders.csv?456"
response = requests.get(url)
file_path = "Orders.csv"

with open(file_path, "wb") as file:
    file.write(response.content)

# Step 2: Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Step 3: Group by "product" and calculate the quantity for each product
product_counts = df.groupby("product").size()

# Step 4: Find the most popular product
most_popular_product = product_counts.idxmax()

print("The most popular product is:", most_popular_product)