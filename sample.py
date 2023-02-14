import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'RELIANCE.NS'

# Get data for the ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2023-02-10', end='2023-02-14')

# Print the DataFrame
print(tickerDf)
