#  ======== WHILE LOOPS

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

p = 2
while p < 6:
    print(p)
    p += 1
else:
    print("p is no longer less than 6")


#  ======== FOR LOOPS

fruits = ["apple", "banana", "grape"]

for f in fruits:
    print("before --", f)
    if f == "banana":
        break
    print("after --", f)

adj = ["red", "big", "juicy"]

for a in adj:
    for b in fruits:
        print(a, b)

# ======== Range

for y in range(2, 6):
    print(y)

for x in range(2, 6):
    print(x)

for z in range(10):
    if z == 5:
        break
    print(z)
else:
    print("finally done")

total = 0
for abc in range(5):
    total = total + abc
print(total)


#  ======== Try/Except

try:
    print("Hello")
except:
    print("An exception occurred")
else:
    print("Nothing went wrong")
finally:
    print("Try/Exception finished")


#  ======== BASIC FUNCTIONS


def my_message():
    print("I'm in drawing class!")


my_message()


def familyName(lName):
    print(lName + " Smith")


familyName("Jerry")
familyName("Amy")
familyName("Chad")
