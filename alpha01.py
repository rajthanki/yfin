import requests
import pandas as pd

symbol_id = '27603'  # Replace with the symbol ID for SBI on Investing.com
api_key = 'YOUR_API_KEY'  # Replace with your Investing.com API key

# Make a request to the Investing.com API
response = requests.get(f'https://www.investing.com/api/v3/stock/historical_data',
                        params={
                            'symbol_id': symbol_id,
                            'period': 'MAX',
                            'interval_unit': 'DAY',
                            'sort': 'DESC',
                            'limit': '7',
                            'country_id': '5',  # India
                            'api_key': api_key
                        })

# Parse the JSON response into a Pandas DataFrame
data = response.json()['candles']
df = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
df['Date'] = pd.to_datetime(df['Date'], unit='s')
df = df.set_index('Date')

# Print the resulting data
print(df)
