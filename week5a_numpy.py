import numpy as np

a = np.array([1, 2, 3, 4, 5])
print("array a ...", a)

b = np.zeros(4)
print("array b of zeros ...", b)

c = np.ones(2)
print("array c of ones ...", c)

#   Creates an array whole initial content is random
#   it depends on the state of memory.
d = np.empty(3)
print("array d empty ...", d)

#   array of 5 numbers starting at 0
e = np.arange(5)
print("array e of range ...", e)

#   Array of evenly inter-spaced values
#   start at 1st value,
#   Upto but not including the second value
#   By steps of the last value
f = np.arange(2, 9, 2)
print("array f of inter-spaced values ...", f)

#   With values that are spaced linearly in a specified interval
#   from 1st value, up to 2nd value, with number of elements
g = np.linspace(0, 10, num=5)
print("array g linearly spaced values ...", g)

#   Contains a range of evenly spaced intervals
h = np.arange(2, 9, 2)
print("array h evenly spaced intervals ...", h)

#   Sorting
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
i = np.sort(arr)
print("array i sorted ...", i)

#   Concatenation
aa = np.array([1, 2, 3, 4])
bb = np.array([5, 6, 7, 8])
arrCombo = np.concatenate((aa, bb))
print("arrays combined ...", arrCombo)

xx = np.array([[1, 2], [3, 4]])
yy = np.array([[5, 6]])
arrCombo2 = np.concatenate((xx, yy), axis=0)
print("array combo of multi dimensional arrays ...\n", arrCombo2)

#   Knowing Shape and size of NumPy arrays
array_example = np.array(
    [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
    ]
)
t = array_example.ndim
print("Dimensions ...", t)  # 3 (dimensions)

u = array_example.size
print("Axis and length ...", u)  # 2, 4 (2 axis w/ length of 4)

v = array_example.shape
print("Dimensions, axis, length ...", v)  # 3, 2, 4

#   Reshaping arrays
j = np.arange(6)
print("\narray j ... ", a)
k = j.reshape(3, 2)  # 3 axis w/ length of 2
print("array j reshaped (3,2)  ...\n", k)

#   Indexing and Slicing ...
data = np.array([1, 2, 3])
a2 = data[1]
b2 = data[0:2]
c2 = data[1:]
d2 = data[-2:]
print("\nOriginal data ...", data)
print("a2 element ...", a2)
print("b2 slice 0:2 ...", b2)
print("c2 1: ...", c2)
print("d2 -2: ...", d2)

data2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("\ndata2 original array ...", data2)
print("data2 elements < 5 ...", data2[data2 < 5])

five_up = data2 >= 5
print("data2 elements >= 5 ...", data2[five_up])

divisible_by_2 = data2[data2 % 2 == 0]
print("data2 elements divisible_by_2 ...", divisible_by_2)

## BROADCASTING
# a shape-(3, 4) array
x = np.array(
    [[-0.0, -0.1, -0.2, -0.3], [-0.4, -0.5, -0.6, -0.7], [-0.8, -0.9, -1.0, -1.1]]
)

# a shape-(4,) array
y = np.array([1, 2, 3, 4])

# multiplying a shape-(4,) array with a shape-(3, 4) array
# `y` is multiplied by each row of `x`
print("arrays x * y ...\n", x * y)

#   Output: -
#   array([ [-0. , -0.2, -0.6, -1.2],
#        	[-0.4, -1. , -1.8, -2.8],
#        	[-0.8, -1.8, -3. , -4.4] ])
