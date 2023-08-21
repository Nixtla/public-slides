import matplotlib.pyplot as plt
from rich import print
from statsforecast import StatsForecast as sf


def plot(df, fcst_df=None, level=None, plot_anomalies=False):
    print('[blue] ==== Dataset ==== [/blue]')
    print(df.head())
    print('\n')
    if fcst_df is not None:
        print('[violet] ==== TimeGPT Forecasts ==== [/violet]')
        print(fcst_df.head())
    print('\n')
    if plot_anomalies:
        fcst_df = df.merge(fcst_df, how='left')
    sf.plot(df, fcst_df, level=level, engine='plotly', plot_anomalies=plot_anomalies, max_insample_length=24 * 10)
    plt.show(block=False)
    plt.pause(0.1)
