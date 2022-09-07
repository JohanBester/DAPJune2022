import pandas as pd

cities = pd.DataFrame(
    [["St. Louis", "Missouri"], ["Atlanta", "Georgia"]], columns=["City", "State"]
)
cities.to_csv("cities.csv", index=False)

df = pd.read_csv("cities.csv")
print(df)
