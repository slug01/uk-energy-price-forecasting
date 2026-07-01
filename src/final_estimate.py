import pandas as pd

master = pd.read_csv(
    "clean_data/master_energy_dataset.csv"
)

master["Timestamp"] = pd.to_datetime(
    master["Timestamp"]
)

recent_week = (
    master
    .sort_values("Timestamp")
    .tail(168)
)

estimate = (
    recent_week["Price_p_kWh"]
    .mean()
)

print(
    f"Final Estimated Exposure: {estimate:.2f} p/kWh"
)