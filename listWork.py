#   Lists in Python

"""
    ALWAYS a strict order 
    BUT can be modified
    CAN have duplicates in a list
    Lists can contain ANY data type
"""

thisList = ["apple", "banana", "cherry"]
print("thisList = ", thisList)
print("\nLength of list = ", len(thisList))
print("\nList item 1 = ", thisList[1])

#   Replace an element in a list
thisList[1] = "blackcurrant"
print("\nList with new item 1 = ", thisList)

#   slice a piece of a list
print("Slice of this list [1:3] ...", thisList[1:3])

#   append item to a list
thisList.append("orange")

#   insert an item at an idex position in a list
thisList.insert(1, "mandarin")
print("\nThe transformed new List = ", thisList)

#   extend a list with another list
tropical = ["mango", "pineapple", "papaya"]
thisList.extend(tropical)
print("\nThe extended list = ", thisList)

#   removing items from a list
thisList.remove("blackcurrant")
thisList.pop(1)  # remove mandarin
thisList.pop()  # remove papaya
del thisList[0]  # remove apple
print("\nList after removing items", thisList)

#   Manipulate the order of a list
thisList.reverse()
print("thisList.reverse() = ", thisList)
thisList.sort()
print("thisList.sort() = ", thisList)
thisList.sort(reverse=True)
print("thisList.sort(reverse=True) = ", thisList)

#   Copy a list
myList = thisList.copy()
print("\nThe two lists are ... \n", thisList, "\nand ...\n", myList)

myList.clear()
print("\nmyList after clear ...\n", myList)
del thisList
# print("\thisList after clear ...", thisList)

#   Concatenating lists together
list1 = ["apple", "banana", "cherry"]
list2 = ["kiwi", "strawberry", "grape"]
list3 = list1 + list2

print("\nThe new list3 = list1 + list2 ... ", list3)


# original list
thisList = ["apple", "cherry", "banana"]

# when you want to sort a list in descending order
thisList.sort(reverse=True)
print("Sort reverse True...", thisList)

# the default of .sort is NOT descending so you can leave ( ) empty
# or you can put (reverse = False)
thisList.sort()
print("This List default sort ... ", thisList)

thisList.sort(reverse=False)
print("Sort reverse False...", thisList)

# using the reverse method just gets you a reversal
thisList.reverse()
print("Just a simple revers ...", thisList)
