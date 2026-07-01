# UK Energy Price Forecasting

## Project Overview

End-to-end machine learning pipeline for forecasting UK electricity prices using historical market data, weather conditions, and energy generation.

## Dataset

- NESO electricity demand
- Weather data
- Market price data

## Project Structure

src/
notebooks/
clean_data/
data_raw/
reports/

## Workflow

Load Data
↓

Clean Data
↓

Feature Engineering
↓

EDA
↓

Model Training
↓

Prediction
↓

Evaluation

## Machine Learning

Random Forest Regressor

Features:
- Demand
- Wind Generation
- Solar Generation
- Temperature
- Wind Speed
- Cloud Cover
- Hour
- Month
- Weekend

Target:
Electricity Price (p/kWh)

## Results

MAE: 1.14 p/kWh

Tomorrow Price Estimate:
10.41 p/kWh

## Technologies

Python
Pandas
NumPy
Matplotlib
Scikit-learn
