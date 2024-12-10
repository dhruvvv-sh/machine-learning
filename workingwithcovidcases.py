import pandas as pd
df = pd.read_csv("C:/Users/satish/github/machine-learning/data_global_data.csv")
print(df.describe())
df_filtered = df[df['deaths'] != 0]
print(df_filtered.to_string)
print(df.describe())