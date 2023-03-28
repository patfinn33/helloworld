#!/usr/bin/env python3

import requests
import locale

print('hello World!')

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()

print(f"Bitcoin price: {data['bpi']['USD']['rate']}")

response = requests.get("https://api.blockchain.info/charts/total-bitcoins?format=json")
data = response.json()

total_bitcoins = data["values"][-1]["y"]
formatted_total_bitcoins = locale.format_string("%d", total_bitcoins, grouping=True)

print(f"Total number of Bitcoins in circulation: {formatted_total_bitcoins}")
