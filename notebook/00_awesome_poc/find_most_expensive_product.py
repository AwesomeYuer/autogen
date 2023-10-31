# filename: find_most_expensive_product.py
import pandas as pd

# 读取CSV文件
df = pd.read_csv("Orders.csv")

# 按商品分组并计算平均价格
average_price = df.groupby("Product")["Price"].mean()

# 找到平均价格最高的商品
most_expensive_product = average_price.idxmax()