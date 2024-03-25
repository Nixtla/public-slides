# Import necessary libraries and authenticate
import os

import ray
from nixtlats import TimeGPT
from src.utils import plot

# Connect to ray cluster
ray.init(address=os.environ['RAY_ADDRESS'])

# Authorize timegpt
timegpt = TimeGPT(token=os.environ['TIMEGPT_TOKEN'])

# Load historical data distributedly (using Ray)
historic_df = ray.data.read_parquet('s3://nixtla-public/anyscale/time-series/')

# Predict the future distributedly (using Ray) 
fcst_df = timegpt.forecast(historic_df, h=24, add_history=True, level=[99])

# Visualize
plot(historic_df, fcst_df)
