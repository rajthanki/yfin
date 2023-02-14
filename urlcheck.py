import requests

url = "https://www.nseindia.com/api/option-chain-indices?symbol=RELIANCE&expiryDate=24FEB2022"

response = requests.get(url)

print(response.text)
