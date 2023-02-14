import requests
import json

# Define the stock symbol
symbol = "RELIANCE"

# Define the expiration date (format: ddMMMyyyy)
expiration = "24FEB2022"

# Define the URL for the option chain API
url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}&expiryDate={expiration}"

# Define headers to bypass user-agent restrictions
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Accept-Language": "en-US,en;q=0.9"
}

# Send a GET request to the API
response = requests.get(url, headers=headers)

# Parse the JSON response
data = json.loads(response.text)

# Extract the option chain data from the JSON
call_records = data['records']['data'][0]['CE']
put_records = data['records']['data'][0]['PE']

# Print the option chain data
print("CALLS:")
for call in call_records:
    print(call)
print()
print("PUTS:")
for put in put_records:
    print(put)
