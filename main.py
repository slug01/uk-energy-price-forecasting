from src.data_loader import load_data
from src.data_cleaning import (
    clean_neso,
    clean_weather,
    clean_price,
    merge_datasets
)
from src.feature_engineering import create_features

print("=" * 50)
print("NATIONWIDE UTILITIES ASSESSMENT")
print("=" * 50)

# Load

neso, weather, price = load_data()

# Clean

neso = clean_neso(neso)
weather = clean_weather(weather)
price = clean_price(price)

# Merge

master = merge_datasets(
    neso,
    weather,
    price
)

# Features

master = create_features(master)

# Save

master.to_csv(
    "clean_data/master_energy_dataset.csv",
    index=False
)

print("\nDataset Created Successfully")
print(master.shape)

print("\nAverage Price")
print(
    round(
        master["Price_p_kWh"].mean(),
        2
    ),
    "p/kWh"
)