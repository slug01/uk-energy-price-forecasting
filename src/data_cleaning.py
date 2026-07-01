import pandas as pd

# ==========================================
# CLEAN NESO DATA
# ==========================================

def clean_neso(neso):

    neso["SETTLEMENT_DATE"] = pd.to_datetime(
        neso["SETTLEMENT_DATE"]
    )

    neso["Timestamp"] = (
        neso["SETTLEMENT_DATE"]
        +
        pd.to_timedelta(
            (neso["SETTLEMENT_PERIOD"] - 1) * 30,
            unit="min"
        )
    )

    neso = neso[
        [
            "Timestamp",
            "ND",
            "EMBEDDED_WIND_GENERATION",
            "EMBEDDED_SOLAR_GENERATION"
        ]
    ].copy()

    neso.columns = [
        "Timestamp",
        "Demand_MW",
        "Wind_MW",
        "Solar_MW"
    ]

    neso["Renewable_MW"] = (
        neso["Wind_MW"]
        + neso["Solar_MW"]
    )

    # Convert 30 min data to hourly

    neso = (
        neso
        .set_index("Timestamp")
        .resample("h")
        .mean()
        .reset_index()
    )

    # Remove dates outside weather range

    neso = neso[
        neso["Timestamp"] >= "2026-03-01"
    ]

    return neso


# ==========================================
# CLEAN WEATHER DATA
# ==========================================

def clean_weather(weather):

    weather["Timestamp"] = pd.to_datetime(
        weather["time"]
    )

    weather = weather[
        [
            "Timestamp",
            "temperature_2m",
            "wind_speed_10m",
            "cloud_cover"
        ]
    ].copy()

    weather.columns = [
        "Timestamp",
        "Temperature_C",
        "WindSpeed",
        "CloudCover"
    ]

    weather = weather.drop_duplicates()

    return weather


# ==========================================
# CLEAN PRICE DATA
# ==========================================

def clean_price(price):

    # Keep APX market prices

    price = price[
        price["DataProvider"] == "APXMIDP"
    ].copy()

    price["Timestamp"] = pd.to_datetime(
        price["StartTime"],
        utc=True
    )

    price["Timestamp"] = (
        price["Timestamp"]
        .dt.tz_localize(None)
    )

    price = price[
        [
            "Timestamp",
            "Price",
            "Volume"
        ]
    ].copy()

    # Convert £/MWh to p/kWh

    price["Price_p_kWh"] = (
        price["Price"] / 10
    )

    # Convert 30 min data to hourly

    price = (
        price
        .set_index("Timestamp")
        .resample("h")
        .mean(numeric_only=True)
        .reset_index()
    )

    return price


# ==========================================
# MERGE DATASETS
# ==========================================

def merge_datasets(
    neso,
    weather,
    price
):

    master = pd.merge(
        neso,
        weather,
        on="Timestamp",
        how="inner"
    )

    master = pd.merge(
        master,
        price[
            [
                "Timestamp",
                "Price_p_kWh"
            ]
        ],
        on="Timestamp",
        how="inner"
    )

    # Final cleaning

    master = master.drop_duplicates()

    return master