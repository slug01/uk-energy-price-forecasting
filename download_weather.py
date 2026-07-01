import requests
import pandas as pd
import os

os.makedirs("data_raw", exist_ok=True)

url = (
    "https://archive-api.open-meteo.com/v1/archive"
    "?latitude=52.48"
    "&longitude=-1.89"
    "&start_date=2026-03-01"
    "&end_date=2026-06-01"
    "&hourly=temperature_2m,wind_speed_10m,cloud_cover"
)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = pd.DataFrame(data["hourly"])

    weather.to_csv(
        "data_raw/weather_data.csv",
        index=False
    )

    print("Weather data saved successfully!")
else:
    print("Error:", response.status_code)