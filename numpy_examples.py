import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 10, 12]])
print(a[0])
print("a =", a)


b = np.zeros(4)
# print("b =", b)

c = np.ones(2)
# print("c =", c)

d = np.empty(3)
# print("d =", d)


# Array of 5 numbers starting at 0
e = np.arange(5)
# print("e =", e)


# Array of evenly inter-spaced values
# start at 1st value,
# Upto but not including the second value
# By steps of the last value
f = np.arange(2, 9, 2)
# print("f =", f)

# Create a Linearly spaced array
# With values that are spaced linearly in a specified interval
# from 1st value, up to 2nd value, with specified number of elements
g = np.linspace(0, 10, num=5)
# print("g =", g)


# Concatenation
a2 = np.array([1, 2, 3, 4])
b2 = np.array([5, 6, 7, 8])
arr2 = np.concatenate((a2, b2))
# print("arr2 =", arr2)

# More Concatenation
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
arr3 = np.concatenate((x, y), axis=0)
# print("arr3", arr3)


#   Knowing Shape and size of NumPy arrays
array_example = np.array(
    [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
    ]
)

t = array_example.ndim
# print("t =", t)
u = array_example.size
# print("u =", u)
v = array_example.shape
# print("v =", v)


#   Reshaping arrays

jj = np.arange(6)
# print("\narray jj ... ", jj)

kk = jj.reshape(3, 2)  # 3 axis w/ length of 2
# print("array j reshaped (3,2)  ...\n", kk)


#   Indexing and Slicing Arrays ...
data = np.array([1, 2, 3])
aa2 = data[1]
bb2 = data[0:2]
cc2 = data[1:]
dd2 = data[-2:]
# print("\nOriginal data ...", data)
# print("a2 element ...", aa2)
# print("b2 slice 0:2 ...", bb2)
# print("c2 1: ...", cc2)
# print("d2 -2: ...", dd2)

data2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print("\ndata2 original array ...", data2)
# print("data2 elements < 5 ...", data2[data2 < 5])

five_up = data2 >= 5
# print("data2 elements >= 5 ...", data2[five_up])

divisible_by_2 = data2[data2 % 2 == 0]
# print("data2 elements divisible_by_2 ...", divisible_by_2)


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

# print("arrays x * y ...\n", x * y)

#   Output: -
#   array([ [-0. , -0.2, -0.6, -1.2],
#        	[-0.4, -1. , -1.8, -2.8],
#        	[-0.8, -1.8, -3. , -4.4] ])
