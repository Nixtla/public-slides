# Probabilistic conformal prediction for hierarchical time series with TimeGPT

# Import necessary libraries and authenticate
import os

from nixtlats import TimeGPT
from src.utils import (
    plot, read_data,
    add_conformal_intervals,
    reconcile_forecasts,
)

timegpt = TimeGPT(token=os.environ['TIMEGPT_TOKEN'])

# Load historical data
historic_df, S_df, tags = read_data()
holdout_historic_df = read_data(holdout=True)

# Predict the future 
forecasts_df = timegpt.forecast(historic_df, h=8)
holdout_forecasts_df = timegpt.forecast(holdout_historic_df, h=8)

# Reconcile forecasts
forecasts_df = reconcile_forecasts(forecasts_df, S_df, tags)
holdout_forecasts_df = reconcile_forecasts(holdout_forecasts_df, S_df, tags)

# Add prediction intervals
level = [80, 90, 99]
forecasts_df = add_conformal_intervals(forecasts_df, holdout_forecasts_df, historic_df, level)

# Visualize
plot(historic_df, S_df, tags, forecasts_df, level)
