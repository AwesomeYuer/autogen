# filename: calculate_average_price.py
import pandas as pd

# Read the CSV file
df = pd.read_csv("Orders.csv")

# Calculate the average price for each product
average_price = df.groupby("Product")["Price"].mean()