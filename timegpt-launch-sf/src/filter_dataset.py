import pandas as pd

df = pd.read_csv('./electricity-markets.csv')
df = df.query('unique_id != "NP"')
df.to_csv('./electricity-markets.csv', index=False)
