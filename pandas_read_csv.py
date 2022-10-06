import pandas as pd

# Working with CSV files

df = pd.read_csv("DAP_SampleData\data.csv")
# print("Raw Data Frame ...", df)
# print("Data Frame to string ...", df.to_string())

pd.options.display.max_rows = 9999
# print(pd.options.display.max_rows)
# print(df)

# print("\nTop 11 rows ...\n", df.head(11))
# print("\nThe header 5 rows ...\n", df.head())
# print("The last 10 rows ...", df.tail(10))

# print("Data Frame Summary ...", df.info())
# print("Data Frame to string ...", df.to_string())


"""
    There are 5 rows in the Calories column without data
    Nulls are bad
    Nulls = the wrong result when you analyze data
"""
# To drop NULLS from the original DF in place
# df.dropna(inplace=True)
# print("\nDF without NULLs ...\n", df.to_string())

# new_df = df
# print("\nNew DF ...\n", new_df)

# To fill in NULLS in place
# df.fillna(13000, inplace=True)
# new_df = df
# print("\nNew DF ...\n", new_df)


# print(df)
# print(df.info())
# print(df.head())
# print(df.to_string())

# print(new_df)
