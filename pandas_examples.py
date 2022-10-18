import pandas as pd

Report = {
    "Classes": ["Math", "Science", "Spanish", "History", "Health"],
    "Grades": [75, 80, 95, 60, 100],
}

results = pd.DataFrame(Report)
print(results)


# Finding the location
print("\n", results.loc[3])


# Print More than 1 line
print("\n", results.loc[[2, 3]])


# Naming the Rows
results2 = pd.DataFrame(Report, index=["week1", "week2", "week3", "week4", "week5"])
print("\n", results2)


# Locating a specific named row
print("\n", results2.loc["week3"])


# Series Example
age = [20, 40, 60]
years = pd.Series(age)

print("Years ...\n", years)
print("\nElement number 1 ...", age[0])


# Naming the Rows
years = pd.Series(age, index=["Me", "My Brother", "My Sister"])
print("My Brother ...", years["My Brother"])
print("Index number 1 ...", years[1])

# Locating a specific row
print("My Sister ...", years["My Sister"])
