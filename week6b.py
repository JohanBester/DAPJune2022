import pandas as pd
import numpy as np
import math
import random

# Series Example
age = [20, 40, 60]
years = pd.Series(age)
print("Years ...\n", years)
print("\nIndex number 1 ...", age[0])

# Naming the Rows
years = pd.Series(age, index=["Me", "My Brother", "My Sister"])
print("My Brother ...", years["My Brother"])
print("Index number 1 ...", years[1])

# Locating a specific row
print("My Sister ...", years["My Sister"])
