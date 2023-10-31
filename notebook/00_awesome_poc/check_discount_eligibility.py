# filename: check_discount_eligibility.py
import pandas as pd

# 读取CSV文件
df = pd.read_csv("Orders.csv")

# 按商品分组并计算平均价格
average_price = df.groupby("Product")["Price"].mean()

# 找到平均价格最高的商品
most_expensive_product = average_price.idxmax()

# 检查商品是否适合打折促销
if average_price[most_expensive_product] > 100:
    print(f"The product '{most_expensive_product}' is eligible for discount promotion.")
else:
    print(f"The product '{most_expensive_product}' is not eligible for discount promotion.")