import re

from rich import print
from nixtla import NixtlaClient


nixtla_client = NixtlaClient(base_url="", api_key="")


def get_number_col(col: str):
    num = re.search(r"\d+$", col)
    if num:
        return int(num.group())
    return None


def plot(df, fcst_df=None, plot_anomalies=False):
    print("[blue] ==== Dataset ==== [/blue]")
    print(df.head())
    print("\n")
    level = None
    if fcst_df is not None:
        print("[violet] ==== TimeGPT Forecasts ==== [/violet]")
        print(fcst_df.head())
        fcst_df.to_csv("fcst-electricity.csv", index=False)
        print("\n")
        level = list(set(get_number_col(col) for col in fcst_df.columns))
        level = [lv for lv in level if lv is not None]
        if len(level) == 0:
            level = None
    fig = nixtla_client.plot(
        df=df[["unique_id", "ds", "y"]],
        forecasts_df=fcst_df,
        level=level,
        engine="plotly",
        max_insample_length=24 * 10,
    )
    fig.show()
