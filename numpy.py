import numpy as np

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

array_example = np.array(
    [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
    ]
)

t = array_example.ndim
print(t)
u = array_example.size
print(u)
v = array_example.shape
print(v)


aa = np.array([1, 2, 3, 4, 5])
print("array a ...", aa)

bb = np.zeros(4)
print("array b of zeros ...", bb)

cc = np.ones(2)
print("array c of ones ...", cc)

#   Creates an array whole initial content is random
#   it depends on the state of memory.
dd = np.empty(3)
print("array d empty ...", dd)

#   array of 5 numbers starting at 0
ee = np.arange(5)
print("array e of range ...", ee)

#   Array of evenly inter-spaced values
#   start at 1st value,
#   Upto but not including the second value
#   By steps of the last value
ff = np.arange(2, 9, 2)
print("array f of inter-spaced values ...", ff)

#   With values that are spaced linearly in a specified interval
#   from 1st value, up to 2nd value, with number of elements
gg = np.linspace(0, 10, num=5)
print("array g linearly spaced values ...", gg)

#   Contains a range of evenly spaced intervals
hh = np.arange(2, 9, 2)
print("array h evenly spaced intervals ...", hh)

# Sorting an Array
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
ii = np.sort(arr)
print("array i sorted ...", ii)

#   Concatenation
aaa = np.array([1, 2, 3, 4])
bbb = np.array([5, 6, 7, 8])
arrCombo = np.concatenate((aaa, bbb))
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
tt = array_example.ndim
print("Dimensions ...", tt)  # 3 (dimensions)

uu = array_example.size
print("Axis and length ...", uu)  # 2, 4 (2 axis w/ length of 4)

vv = array_example.shape
print("Dimensions, axis, length ...", vv)  # 3, 2, 4

#   Reshaping arrays
jj = np.arange(6)
print("\narray jj ... ", jj)
kk = jj.reshape(3, 2)  # 3 axis w/ length of 2
print("array j reshaped (3,2)  ...\n", kk)

#   Indexing and Slicing ...
data = np.array([1, 2, 3])
aa2 = data[1]
bb2 = data[0:2]
cc2 = data[1:]
dd2 = data[-2:]
print("\nOriginal data ...", data)
print("a2 element ...", aa2)
print("b2 slice 0:2 ...", bb2)
print("c2 1: ...", cc2)
print("d2 -2: ...", dd2)

data2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("\ndata2 original array ...", data2)
print("data2 elements < 5 ...", data2[data2 < 5])

five_up = data2 >= 5
print("data2 elements >= 5 ...", data2[five_up])

divisible_by_2 = data2[data2 % 2 == 0]
print("data2 elements divisible_by_2 ...", divisible_by_2)


## BROADCASTING ARRAYS

# a shape-(3, 4) array
x = np.array(
    [[-0.0, -0.1, -0.2, -0.3], [-0.4, -0.5, -0.6, -0.7], [-0.8, -0.9, -1.0, -1.1]]
)
# a shape-(4,) array
y = np.array([1, 2, 3, 4])

# multiplying a shape-(4,) array -- y
# with a shape-(3, 4) array -- x
# `y` is multiplied by each row of `x`
print("arrays x * y ...\n", x * y)

#   Output: -
#   array([ [-0. , -0.2, -0.6, -1.2],
#        	[-0.4, -1. , -1.8, -2.8],
#        	[-0.8, -1.8, -3. , -4.4] ])
