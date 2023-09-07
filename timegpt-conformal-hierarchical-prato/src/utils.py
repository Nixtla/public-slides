from typing import List, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datasetsforecast.hierarchical import HierarchicalData
from hierarchicalforecast.core import HierarchicalReconciliation
from hierarchicalforecast.methods import MinTrace
from hierarchicalforecast.utils import HierarchicalPlot
from rich import print
from statsforecast import StatsForecast as sf


def read_data(holdout=False):
    print('Reading data! :D')
    Y_df, Y_train_df, S_df, tags = pd.read_pickle('./data/data.pickle')
    if holdout:
        return Y_train_df
    return Y_df, S_df, tags

def plot(df, S_df, tags, fcst_df=None, level=None, plot_anomalies=False):
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
    hplot = HierarchicalPlot(S_df, tags)
    cols = ['unique_id', 'ds']
    plot_df = pd.concat([df.set_index(cols), fcst_df.set_index(cols)], axis=1).reset_index('ds') if fcst_df is not None else df.set_index('unique_id')
    hplot.plot_hierarchically_linked_series(
        'vic-hol-noncity',
        plot_df,
        models=['y', 'TimeGPT'] if fcst_df is not None else ['y'],
        level=level,
    )
    plt.show()

def reconcile_forecasts(fcst_df, S_df, tags):
    hrec = HierarchicalReconciliation(reconcilers=[MinTrace(method='ols')])
    rec_df = hrec.reconcile(fcst_df.set_index('unique_id'), S=S_df, tags=tags).reset_index()
    rec_df = rec_df.drop(columns='TimeGPT')
    rec_df.columns = ['unique_id', 'ds', 'TimeGPT']
    return rec_df

def add_conformal_intervals(
	fcst_df: pd.DataFrame,
        cs_df: pd.DataFrame,
        historic_df: pd.DataFrame,
	level: List[Union[int, float]],
	horizon: int = 8,
        models: List[str] = ['TimeGPT'],
    ):
    fcst_df = fcst_df.copy().sort_values(['unique_id', 'ds']).set_index('unique_id')
    cs_df = cs_df.merge(historic_df, how='left', on=['unique_id', 'ds']).assign(cutoff=1)
    cs_df = cs_df.sort_values(['unique_id', 'cutoff', 'ds'])
    alphas = [100 - lv for lv in level]
    cuts = [alpha / 200 for alpha in reversed(alphas)]
    cuts.extend(1 - alpha / 200 for alpha in alphas)
    n_series = fcst_df.index.nunique()
    cs_n_windows = int(len(cs_df) // (n_series * horizon))
    for model in models:
        cs_model = np.abs(cs_df['y'] - cs_df[model]).values
        # cs_windows, n_series, horizon
        scores = cs_model.reshape(cs_n_windows, n_series, horizon)
        mean = fcst_df[model].values.reshape(1, n_series, horizon)
        # scores: n_series, cs_windows, horizon
        lo_scores = (mean - scores)
        hi_scores = (mean + scores)
        scores = np.vstack([lo_scores, mean, hi_scores])
        quantiles = np.quantile(
            scores,
            cuts,
            axis=0,
        )
        quantiles = quantiles.reshape(len(cuts), -1)
        lo_cols = [f"{model}-lo-{lv}" for lv in reversed(level)]
        hi_cols = [f"{model}-hi-{lv}" for lv in level]
        out_cols = lo_cols + hi_cols
        for i, col in enumerate(out_cols):
            sign = -1 if '-lo-' in col else 1
            fcst_df[col] = quantiles[i]
    return fcst_df.reset_index()
