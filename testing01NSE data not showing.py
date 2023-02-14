import requests

# Define the stock symbol
symbol = "AAPL"

# Define the expiration date (format: yyyy-mm-dd)
expiration = "2022-02-18"

# Define the URL for the option chain API
url = f"https://finance.yahoo.com/quote/{symbol}/options?date={expiration}&p={symbol}"

# Define headers to bypass user-agent restrictions
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
}

# Send a GET request to the API
response = requests.get(url, headers=headers)

# Parse the HTML response
html = response.text

# Extract the option chain data from the HTML
calls_start = html.find("calls\":{\"options\":[")
calls_end = html.find("}],\"error\"")
puts_start = html.find("puts\":{\"options\":[")
puts_end = html.find("}],\"error\"")
calls_data = html[calls_start+17:calls_end+1]
puts_data = html[puts_start+16:puts_end+1]

# Print the option chain data
print("CALLS:")
print(calls_data)
print()
print("PUTS:")
print(puts_data)
