# filename: market_research.py

import requests

# 发送GET请求获取市场调研信息
response = requests.get("https://example.com/market_research")

# 打印市场调研信息
print(response.text)