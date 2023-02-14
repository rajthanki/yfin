import requests
import json

# Define the stock symbol
symbol = "RELIANCE"

# Define the expiry date (format: ddMMMyyyy)
expiry = "24FEB2022"

# Define the strike price
strike_price = 3000

# Define the URL for the option chain API
url = f"https://www.nseindia.com/api/option-chain-equity?symbol={symbol}&expiryDate={expiry}"

# Define headers to bypass user-agent restrictions
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
}

# Send a GET request to the API
response = requests.get(url, headers=headers)

# Parse the JSON response
data = json.loads(response.text)

# Get the option chain data for the specified strike price and expiry date
call_data = None
put_data = None
for i in data['records']['data']:
    if i['CE'] and i['CE']['strikePrice'] == strike_price and i['CE']['expiryDate'] == expiry:
        call_data = i['CE']
    if i['PE'] and i['PE']['strikePrice'] == strike_price and i['PE']['expiryDate'] == expiry:
        put_data = i['PE']
    if call_data and put_data:
        break

# Print the call and put option data
if call_data:
    print(f"Call Option (Strike Price {call_data['strikePrice']})")
    print(f"Open Interest: {call_data['openInterest']}")
    print(f"Change in Open Interest: {call_data['changeinOpenInterest']}")
    print(f"Last Price: {call_data['lastPrice']}")
    print(f"Change: {call_data['change']}")
    print(f"Implied Volatility: {call_data['impliedVolatility']}")
    print(f"Greeks (Delta, Theta, Gamma, Vega): {call_data['delta']}, {call_data['theta']}, {call_data['gamma']}, {call_data['vega']}")
    print()

if put_data:
    print(f"Put Option (Strike Price {put_data['strikePrice']})")
    print(f"Open Interest: {put_data['openInterest']}")
    print(f"Change in Open Interest: {put_data['changeinOpenInterest']}")
    print(f"Last Price: {put_data['lastPrice']}")
    print(f"Change: {put_data['change']}")
    print(f"Implied Volatility: {put_data['impliedVolatility']}")
    print(f"Greeks (Delta, Theta, Gamma, Vega): {put_data['delta']}, {put_data['theta']}, {put_data['gamma']}, {put_data['vega']}")
