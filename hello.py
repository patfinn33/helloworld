#!/usr/bin/env python3

import requests

print('hello World!')

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()

print(f"Bitcoin price: {data['bpi']['USD']['rate']}")
