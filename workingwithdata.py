import pandas as pd
df = pd.read_csv('C:/Users/satish/github/machine-learning/data.csv')
df.dropna(inplace=True)
for x in df.index:
  if df.loc[x, "Duration"] > 45:
    df.drop(x, inplace = True)
print(df.to_string())
print(df.describe())