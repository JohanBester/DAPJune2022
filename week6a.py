import pandas as pd

Report = {
    "Classes": ["Math", "Science", "Spanish", "History", "Health"],
    "Grades": [75, 80, 95, 60, 100],
}
results = pd.DataFrame(Report)
print(results)

# Finding Finding the location
print("\n", results.loc[3])

# Print More than 1 line
print("\n", results.loc[[2, 3]])

# Naming the Rows
results2 = pd.DataFrame(Report, index=["week1", "week2", "week3", "week4", "week5"])
print("\n", results2)

# Locating a specific named row
print("\n", results2.loc["week3"])
