import pandas as pd

master = pd.read_csv(
    "clean_data/master_energy_dataset.csv"
)

print("MISSING VALUES")
print(master.isnull().sum())

print("\nDUPLICATES")
print(master.duplicated().sum())

print("\nCORRELATION WITH PRICE")

corr = (
    master
    .corr(numeric_only=True)
    ["Price_p_kWh"]
    .sort_values(ascending=False)
)

print(corr)