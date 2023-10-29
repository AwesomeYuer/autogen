# filename: stock_chart.py
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock symbols and YTD timeframe
symbols = ['NVDA', 'TSLA']
start_date = '2022-01-01'
end_date = '2022-12-31'

# Fetch the stock price data using pandas-datareader
df = pd.DataFrame()
for symbol in symbols:
    symbol_data = pd.read_csv(f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1=1640995200&period2=1672444799&interval=1d&events=history&includeAdjustedClose=true', parse_dates=['Date'])
    symbol_data.set_index('Date', inplace=True)
    df[symbol] = symbol_data['Adj Close']

# Plot the stock price change YTD
plt.plot(df.index, df)

# Set plot labels and title
plt.legend(symbols)
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('YTD Stock Price Change: NVDA vs TSLA')

# Display the chart
plt.show()