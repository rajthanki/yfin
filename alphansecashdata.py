import requests
import pandas as pd

symbol = 'SBIN.BSE'  # Replace with the stock symbol for SBI

# Make a request to the Alpha Vantage API
response = requests.get('https://www.alphavantage.co/query',
                        params={
                            'function': 'TIME_SERIES_DAILY_ADJUSTED',
                            'symbol': symbol,
                            'outputsize': 'compact',
                            'apikey': 'YOUR_API_KEY'  # Replace with your Alpha Vantage API key
                        })

# Parse the JSON response into a Pandas DataFrame
data = response.json()
df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')

# Convert index to datetime and sort by date
df.index = pd.to_datetime(df.index)
df = df.sort_index()

# Extract the daily time series data for the past 6 months
last_date = df.index[-1]
six_months_ago = (last_date - pd.DateOffset(months=6)).strftime('%Y-%m-%d')
six_month_data = df.loc[six_months_ago:last_date]

# Print the resulting data
print(six_month_data)
