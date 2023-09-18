import fugue.api as fa
import matplotlib.pyplot as plt
import pandas as pd
from rich import print
from utilsforecast.plotting import plot_series 


def plot(df, fcst_df=None):
    cols = ['unique_id', 'ds', 'y']
    df = fa.as_pandas(df)[cols]
    df['ds'] = pd.to_datetime(df['ds'])
    print('[blue] ==== Dataset ==== [/blue]')
    print(df.head())
    print('\n')
    if fcst_df is not None:
        fcst_df = fa.as_pandas(fcst_df)
        print('[violet] ==== TimeGPT Forecasts ==== [/violet]')
        print(fcst_df.head())
    print('\n')
    plot_anomalies = fcst_df is not None and 'TimeGPT-lo-99' in fcst_df.columns
    level = [99] if plot_anomalies else None
    fig = plot_series(
        df,
        fcst_df,
        level=level, engine='plotly', plot_anomalies=plot_anomalies, max_insample_length=7 * 24,
        models=['TimeGPT'] if fcst_df is not None else None
    )
    fig.show()
    plt.show(block=False)
    plt.pause(0.1)
