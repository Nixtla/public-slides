from datasetsforecast.hierarchical import HierarchicalData
import pandas as pd


def prepare_data():
    Y_df, S_df, tags = HierarchicalData.load('./data', 'TourismSmall')
    Y_test_df = Y_df.groupby('unique_id').tail(8)
    Y_train_df = Y_df.drop(Y_test_df.index)
    res = Y_df, Y_train_df, S_df, tags
    pd.to_pickle(res, './data/data.pickle')


if __name__=="__main__":
    prepare_data()
