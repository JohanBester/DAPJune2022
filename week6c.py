import pandas as pd

df = pd.read_csv("data.csv")
# print(df)
# print(df.to_string())

pd.options.display.max_rows = 9999
# print(pd.options.display.max_rows)
# print(df)

# print(df.head(11))
# print(df.head())

df = pd.read_csv("data.csv")
# print(df.info())
# print(df.to_string())

#   To dorp NULLS and creates a new DataFrame
new_df = df.dropna()
# print(new_df.info())

# To drop NULLS from the original DF in
df = df.dropna(inplace=True)

# To fill in NULLS in place
new_df = df.fillna(130, inplace=True)

# print(df)
# print(df.info())
# print(df.head())
# print(df.to_string())

print(new_df)
