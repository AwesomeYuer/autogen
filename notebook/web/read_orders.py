# filename: read_orders.py

import pandas as pd

# 读取订单数据文件
orders = pd.read_csv("SamplesData/Orders.csv")

# 打印前几行数据
print(orders.head())