import pandas as pd

df = pd.read_csv('./electricity.csv')
df = df.query('unique_id != "NP"')
df.to_csv('./electricity.csv', index=False)
