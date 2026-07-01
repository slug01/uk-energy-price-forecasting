
Objective

The objective of this assessment was to estimate the average electricity price exposure (p/kWh) for a large manufacturing facility in Great Britain for the target date.

Because no fixed electricity contract was assumed, the factory is exposed to wholesale market price fluctuations influenced by electricity demand, renewable generation, weather conditions and market dynamics.

---

Data Sources

The following publicly available datasets were collected and combined:

NESO (National Energy System Operator)

   * National electricity demand
   * Embedded wind generation
   * Embedded solar generation

 Elexon Market Index Price Data

   * APX market prices
   * Settlement period electricity prices

3. Open-Meteo Weather Data

   * Temperature
   * Wind speed
   * Cloud cover

The common analysis period was March 2026 to May 2026.

---

Data Preparation

Several preprocessing steps were performed:

* Converted timestamps into a common hourly format
* Aggregated half-hourly settlement data into hourly observations
* Renamed and standardised variables
* Created renewable generation features
* Removed duplicate records
* Merged demand, generation, weather and price datasets into a single master dataset

Final dataset size:

2,125 hourly observations

---

Exploratory Analysis

Correlation analysis identified the main drivers of electricity prices.

Positive relationship:

* Electricity Demand

Negative relationship:

* Wind Generation
* Renewable Generation
* Wind Speed

These relationships are consistent with expected energy market behaviour.

---

Machine Learning Approach

A Random Forest Regressor was developed to estimate electricity prices using:

* Demand_MW
* Wind_MW
* Solar_MW
* Temperature_C
* WindSpeed
* CloudCover
* Hour
* Month
* Weekend

Model performance was evaluated using a holdout dataset.

Mean Absolute Error (MAE):

1.14 p/kWh

Feature importance analysis indicated that wind generation and demand were the strongest predictors of electricity price.

---

Final Estimate

Estimated Electricity Price Exposure:

10.41 p/kWh

This estimate represents the expected electricity price exposure for the target date based on historical demand, renewable generation, weather conditions and market price behaviour.

---

Assumptions

* Latest observed system conditions were used as a proxy for next-day conditions.
* Historical relationships between demand, renewable generation and prices remain valid.
* No major generation outages or extreme market events occur on the target date.

---

Limitations

* Day-ahead weather forecasts were not incorporated.
* Fuel prices and interconnector flows were not included.
* The model uses historical observations and may not capture unexpected market shocks.

---

Conclusion

Using a combined dataset of electricity demand, renewable generation, weather observations and market prices, a Random Forest model estimated the factory's electricity price exposure at:

10.41 p/kWh

The model achieved a Mean Absolute Error of 1.14 p/kWh, indicating reasonable predictive performance for short-term electricity price estimation.
