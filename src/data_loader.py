import pandas as pd

def load_data():
    neso = pd.read_csv("data_raw/neso.csv")
    weather = pd.read_csv("data_raw/weather_data.csv")
    price = pd.read_csv("data_raw/combined_price.csv")

    return neso, weather, price