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
