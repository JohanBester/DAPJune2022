import pandas as pd

col_names = [
    "Id",
    "Survived",
    "Passenger Class",
    "Full Name",
    "Gender",
    "Age",
    "SibSp",
    "Parch",
    "Ticket Number",
    "Price",
    "Cabin",
    "Station",
]

titanic_data = pd.read_csv(r"./titanic.csv", names=col_names, skiprows=[0])
titanic_data.to_csv("use_titanic.cvs", index=False)
