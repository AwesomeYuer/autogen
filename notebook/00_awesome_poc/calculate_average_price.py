# filename: calculate_average_price.py
import pandas as pd

# 读取CSV文件
df = pd.read_csv("Orders.csv")

# 按商品分组并计算平均价格
average_price = df.groupby("Product")["Price"].mean()