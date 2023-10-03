# Import necessary libraries and authenticate
import os

import pandas as pd
from nixtlats import TimeGPT

timegpt = TimeGPT(token=os.environ['TIMEGPT_TOKEN'])

# Load historical data
historic_df = pd.read_csv('electricity.csv')

# Predict the future 
fcst = timegpt.forecast(historic_df, h=48, level=[99], add_history=True)

# Visualize
fig = timegpt.plot(historic_df, fcst, plot_anomalies=True, level=[99])
fig.show()



