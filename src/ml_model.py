import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load

master = pd.read_csv(
    "clean_data/master_energy_dataset.csv"
)

master = master.dropna()

# Features

features = [
    "Demand_MW",
    "Wind_MW",
    "Solar_MW",
    "Temperature_C",
    "WindSpeed",
    "CloudCover",
    "Hour",
    "Month",
    "Weekend"
]

X = master[features]

y = master["Price_p_kWh"]

# Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)

# Predict

predictions = model.predict(X_test)

# Evaluate

mae = mean_absolute_error(
    y_test,
    predictions
)

print("\nMODEL PERFORMANCE")
print("-" * 50)

print(f"MAE: {mae:.2f} p/kWh")

# Tomorrow estimate

latest = X.iloc[[-1]]

tomorrow_prediction = model.predict(
    latest
)[0]

print("\nTOMORROW ESTIMATE")
print("-" * 50)

print(
    f"{tomorrow_prediction:.2f} p/kWh"
)

# Feature importance

importance = pd.DataFrame(
    {
        "Feature": features,
        "Importance": model.feature_importances_
    }
)

print("\nFEATURE IMPORTANCE")
print(
    importance.sort_values(
        "Importance",
        ascending=False
    )
)