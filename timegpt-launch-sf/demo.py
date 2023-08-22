# Forecast energy demand from different countries in 5 lines of code with TimeGPT

# Import necessary libraries and authenticate
import os

import pandas as pd
from nixtlats import TimeGPT
from src.utils import plot

timegpt = TimeGPT(os.environ['TIMEGPT_TOKEN'])

# Load historical data
historic_df = pd.read_csv('electricity.csv')

# Predict the future 
forecast_df = timegpt.forecast(
    historic_df, 
    h=24,
    level=[90],
    add_history=True,
)

# Visualize
plot(historic_df, forecast_df, plot_anomalies=True)





