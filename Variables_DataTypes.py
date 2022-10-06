#  Multi Word Variable Names
print("Assigning Variables in Python:-\n")

fruits = ["apple", "banana", "cherry"]
a = b = c = fruits
print(a)
print(b)
print(c)

d, e, f = "Orange", "Banana", "Cherry"
print(d)
print(e)
print(f)

g = h = i = "Orange"
print(g)
print(h)
print(i)

#  Concatenating output Variables
print("\nConcatenating in Python:-\n")

j = "awesome"
print("Python is " + j)

k = "Python is "
l = "awesome"
m = k + l
print("m = k + l: ", m)

n = 5
o = 10
print("n + o =", n + o)

# This errors in Python before version 3.10
p = "5"
q = "John"
print("p + q =", p + q)

#  Global Variables hold values throughout the lifetime of the program
print("\nGlobal variables:-\n")

r = "Wonderful"


def myFunc():
    print("Global variable r =", r)
    print("Python is " + r)


myFunc()


def myFunc2():
    s = "Fantastic"
    print("In scope value of s =", s)
    print("Python is " + s)


myFunc2()


def myFunc3(s):
    print("Reassigned value of s =", s)
    print("Python is " + s)


myFunc3("Amazing")

#  Data Types
"""
You can check the data type of a value by using -- print(type(x))
"""
print("\nPython Data Types can be checked with type(x): -\n")

x = "Hello World"
print("'Hello World' =", type(x))
#  string (str)

x = 20
print("20 =", type(x))
#  integer (int)

x = 20.5
print("20.5 =", type(x))
#  float

x = ["apple", "banana", "cherry"]
print("['apple', 'banana', 'cherry'] =", type(x))
#  list

x = ("apple", "banana", "cherry")
print("('apple', 'banana', 'cherry') =", type(x))
#  tuple

x = range(5)
print("range(5) =", type(x))
#  range

x = {"name": "John", "age": 36}
print("{'name' : 'John',  'age' : 36} =", type(x))
#  dictionary (dict)

x = True
print("True =", type(x))
#  boolean

#  CASTING data types to different types
#  You can put a data type in front of a value if you want to specify

print("\nCasting Data Types in Python:-\n")

x = str("hello, world!")
print("String = ", x)
y = int(20.5)
print("int(20.5) =", y)

z = float(20)
print("float(20) =", z)
