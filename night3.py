# ====== TUPLES

from concurrent.futures.process import _global_shutdown


thisTuple = ("anApple", "aBanana", "laCherry")
fruits = ("apple", "banana", "cherry")

daTuples = thisTuple + fruits
# print("daTuples", daTuples)

(green, yellow, red) = fruits
# print("green", green)    # apple
# print("yellow", yellow)   # banana
# print("red", red)      # cherry

myTuple = fruits * 2
# print("myTuple", myTuple)

# ====== SETS

thisSet = {"apple", "banana", "cherry"}
# print("thisSet1", thisSet)

thisSet.add("orange")
# print("thisSet2", thisSet)

myList = ["kiwi", "orange"]
thisSet.update(myList)
# print("thisSet3", thisSet)

# ====== DICTIONARIES
thisDic = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

# print("thisDic", thisDic)
# print("thisDic-brand", thisDic["brand"])
# print("thisDic len =", len(thisDic))

x = thisDic["model"]
# print("x = ", x)
y = thisDic.get("model")
# print("y = ", y)

thisDic["year"] = "2018"
thisDic["color"] = "red"
# print("thisDic", thisDic)

thisDic.pop("brand")    # remove brand
thisDic.popitem()   # remove color
# print("thisDic", thisDic)

# ========= IF STATEMENTS

a, b = 45, 68
# if a < b:
#     print("b is greater")

c = d = 55
# if d > c:
#     print("d is greater than c")
# elif d == c:
#     print("c and d are equal")

e = 200
f = e/4
# if f > e:
#     print("f is greater than e")
# elif f == e:
#     print("f and e are equal")
# else:
#     print("e is greater than f")

g = 200
h = 33
i = 500
# if g > h and i > g:
#     print("Both conditions are true")
# if g > h or i > g:
#     print("At least one condition are true")

j = 55
if j > 10:
    print("it's above 10")
    if j < 20:
        print("but it's less than 20")
    else:
        print("and it's above 20")
