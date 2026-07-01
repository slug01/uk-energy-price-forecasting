import pandas as pd
import glob

files = glob.glob("data_raw/price_data/*.csv")

price = pd.concat(
    [pd.read_csv(f) for f in files],
    ignore_index=True
)

print(price.shape)

price.to_csv(
    "data_raw/combined_price.csv",
    index=False
)