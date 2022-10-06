# ====== TUPLES

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
thisDic = {"brand": "Ford", "model": "Mustang", "year": "1964"}

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

thisDic.pop("brand")  # remove brand
thisDic.popitem()  # remove color
# print("thisDic", thisDic)
