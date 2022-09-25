#   Matplotlib

import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3]  # x axis values
y = [2, 4, 1]  # corresponding y axis values

plt.plot(x, y)  # plotting the points
plt.xlabel("x - axis")  # naming the x axis
plt.ylabel("y - axis")  # naming the y axis
plt.title("My first graph!")  # giving a title to my graph
plt.show()  # function to show the plot
