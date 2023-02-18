import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbol
tickerSymbol = 'RELIANCE.NS'

# Get data for the ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2022-01-01', end='2022-02-01')

# Create a line chart
plt.plot(tickerDf['Close'])

# Add a title and axis labels
plt.title('Reliance Industries Stock Price')
plt.xlabel('Date')
plt.ylabel('Closing Price (INR)')

# Show the chart
plt.show()

