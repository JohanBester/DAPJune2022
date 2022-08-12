# original list
thislist = ["apple", "cherry", "banana"]

# when you want to sort a list in descending order
thislist.sort(reverse=True)
print("Sort reverse True...", thislist)

# the default of .sort is NOT descending so you can leave ( ) empty
# or you can put (reverse = False)
thislist.sort()
print("This List default sort ... ", thislist)

thislist.sort(reverse=False)
print("Sort reverse False...", thislist)

# using the reverse method just gets you a reversal
thislist.reverse()
print("Just a simple revers ...", thislist)
