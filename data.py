import requests
import pandas as pd

url = "https://data.elexon.co.uk/bmrs/api/v1/balancing/pricing/market-index"

response = requests.get(url)

print(response.status_code)
print(response.text[:500])