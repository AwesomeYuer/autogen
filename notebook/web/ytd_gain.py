# filename: ytd_gain.py
import yfinance as yf
import pandas as pd

# Define the ticker symbols for the 9 largest technology companies (excluding FB)
ticker_symbols = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'GOOG', 'TSM', 'NVDA', 'PYPL', 'INTC']

# Fetch the historical data for the ticker symbols
data = {}
for symbol in ticker_symbols:
    try:
        data[symbol] = yf.download(symbol, start='2021-01-01', end='2021-12-31')
    except Exception as e:
        print(f"Failed to download data for {symbol}: {e}")

# Calculate the YTD gain for each ticker symbol
ytd_gains = {}
for symbol, ticker_data in data.items():
    try:
        ytd_gain = (ticker_data['Close'][-1] - ticker_data['Close'][0]) / ticker_data['Close'][0] * 100
        ytd_gains[symbol] = ytd_gain
    except Exception as e:
        print(f"Failed to calculate YTD gain for {symbol}: {e}")

# Sort the YTD gains in descending order
sorted_ytd_gains = sorted(ytd_gains.items(), key=lambda x: x[1], reverse=True)

# Print the YTD gains for the 9 largest technology companies (excluding FB)
for symbol, ytd_gain in sorted_ytd_gains:
    print(f"{symbol}: {ytd_gain:.2f}%")