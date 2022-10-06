myColors = {"0": "red", "1": "yellow", "2": "green", "3": "white"}

print("\nPrinting my colorful Dictionary ... \n", myColors)

# Add a color
myColors[4] = "blue"

myKeys = myColors.keys()
print("\nPrinting my Keys ... \n", myKeys)

myValues = myColors.values()
print("\nPrinting my Values ... \n", myValues, "\n ")

for k in myKeys:
    print(k)

for v in myValues:
    print(v)
