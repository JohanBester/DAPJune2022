import pandas as pd
import numpy as np
import math
import random

# x = 39
# x += 5
# print(x)
# y = 100
# y -= 75
# print(y)

# print(math.pi)

prob = random.random()
# print(prob)

diceThrow = random.randrange(1, 10)
# print(diceThrow)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 10, 12]])
# print(a[0])
# print(a)

b = np.zeros(4)
# print(b)

d = np.empty(3)
# print(d)

e = np.arange(5)
# print(e)

f = np.arange(2, 9, 2)
# print(f)

g = np.linspace(0, 10, num=5)
# print(g)

arr1 = np.array([2, 1, 5, 3, 7, 4, 6, 8])
a1 = np.sort(arr1)
# print(a1)

a2 = np.array([1, 2, 3, 4])
b2 = np.array([5, 6, 7, 8])
arr2 = np.concatenate((a2, b2))
# print(arr2)

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
arr3 = np.concatenate((x, y), axis=0)
# print(arr3)

array_example = np.array([
    [[0, 1, 2, 3],
     [4, 5, 6, 7]],
    [[0, 1, 2, 3],
     [4, 5, 6, 7]],
    [[0, 1, 2, 3],
     [4, 5, 6, 7]]
])

t = array_example.ndim
print(t)
u = array_example.size
print(u)
v = array_example.shape
print(v)
