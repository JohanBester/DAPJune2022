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

j = "awesome"
print("Python is " + j)

k = "Python is "
l = "awesome"
m = k+l
print(m)

n = 5
o = 10
print(n+o)

p = "5"
q = "John"
print(p+q)

r = "Wonderful"


def myFunc():
    print("Python is " + r)


myFunc()


def myFunc2():
    s = "Fantastic"
    print("Python is " + s)


myFunc2()


def myFunc3(s):
    print("Python is " + s)


myFunc3("Amazing")


t = int(20.5)
print(t)
u = float(20)
print(u)
print(type(t))
print(type(u))

v = "Hello World!"
print(len(v))
print(v[1])
print(v[-1])
print(v[4])

txt = "The smartest class in Saint Louis"
if "best" in txt:
    print("yes, 'best' is present")
else:
    print("The word 'best' is not present")

w = "Hello World!"
print(w[2:5])
print(w[:5])
print(w[6:])
print(w[-5:-2])

x = "Hello World!"
print(x.replace("H", "J"))
print(x.replace("lo", "p"))

y = "Hello"
z = "World"
snakeCase = y+z
print(snakeCase)

age1 = "36"
txt1 = "My name is John, I am " + age1
print(txt1)

age2 = 36
txt2 = "My name is John, I am {}"
print(txt2.format(age2))

quantity = 3
itemNo = 567
price = 49.95
myOrder = "I want {} pieces of item {} for {} dollars."
print(myOrder.format(quantity, itemNo, price))
