# filename: download_and_read_orders.py
import requests
import pandas as pd

# Download the orders data file
url = "http://192.168.0.105:5000/SamplesData/Orders.csv"
response = requests.get(url)
file_path = "Orders.csv"

# Save the file locally
with open(file_path, "wb") as file:
    file.write(response.content)

# Read the CSV file
df = pd.read_csv(file_path)