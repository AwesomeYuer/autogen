# filename: download_and_read_orders.py
import requests
import pandas as pd

# 下载订单数据文件
url = "http://192.168.0.105:5000/SamplesData/Orders.csv"
response = requests.get(url)
file_path = "Orders.csv"

# 将文件保存到本地
with open(file_path, "wb") as file:
    file.write(response.content)

# 读取CSV文件
df = pd.read_csv(file_path)