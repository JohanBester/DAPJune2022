import pandas as pd
import numpy as np
import math
import random

age = [20, 40, 60]
years = pd.Series(age)
# print(years)
# print(age[0])

years = pd.Series(age, index=["Me", "My Brother", "My Sister"])
print(years["My Brother"])
print(years[1])
