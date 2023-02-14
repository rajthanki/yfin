import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data for the ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2022-01-01', end='2022-02-01')

# Print the DataFrame
print(tickerDf)
