# ======= STRINGS

s = "Anything in quotes is a string"
print(s)

# Multi-line comments
"""
Check the data type of a value 
by using -- print(type(x))

"""
print("\nPython Data Types can be checked with type(x): -\n")

x = "Hello World"
print("'Hello World' =", type(x))
#  string (str)

#  Concatenating output with a plus sign
print("\nConcatenating in Python:-\n")

j = "awesome"
print("Python is " + j)

k = "Python is "
l = "awesome"
m = k + l
print("m = k + l: ", m)

# don't confuse this with math
n = 5
o = 10
print(type(n + o))

# This errors in Python before Python version 3.10
p = 5  # number
q = "John"  # string
print("p + q =", p + q)


#  CASTING data types to different types
#  You can put a data type in front of a value if you want to specify
print("\nCasting Data Types in Python:-\n")

# Casting something to a string
x = "hello, world!"
y = str(5)
print("X + Y = ", x + y)
# before Python 3.10 this would fail without casting


#  Finding the length of a string
v = "Hello World!"
print("\nLength of 'Hello World!' = ", len(v))


#   Getting the character index position of a string
print("Character at 1: ", v[1])
print("Character at -1: ", v[-1])
print("Character at 4: ", v[4])


#   Checking for a word/phrase in a string
print("\nSearch for a word in a string:\n")
txt = "The smartest class in Saint Louis"
if "best" in txt:
    print("yes, 'best' is present")
else:
    print("The word 'best' is not present")


# Using the .find() method to search a string
text = "Hello, welcome to my world."
x = text.find("elc")
print(x)


#   Slicing a string and returning a range of characters
print("\nSlicing strings and returning a range of characters\n")
w = "Hello World!"
print("String = ", w)
#   Range starts at number on left, but doesn't include number on right!
print("w[2:5] = ", w[2:5])
#   No number on the left means start from begining
print("w[:5] = ", w[:5])
#   No number on right means go to the end
print("w[6:] = ", w[6:])
#   Negative indexing: count back 5 but exclude last 2 characters
print("w[-5:-2] = ", w[-5:-2])


#   Replacement in a string
wHJ = w.replace("H", "J")
print("Replace H with J ...", wHJ)
wLop = w.replace("lo", "p")
print("Replace lo with p ...", wLop)


#   Formatting a string in Python
print("\nFormatting a String:\n")
age1 = "36"
txt1 = "My name is John, I am " + age1
print("Concatenation example ...", txt1)

age2 = 36
txt2 = "My name is John, I am {}"
print("Formatting example ...", txt2.format(age2))

print("\nComplex Formatting example ...")
quantity = 3
itemNo = 567
price = 49.95
myOrder = "I want {} pieces of item {} for {} dollars."
print(myOrder.format(quantity, itemNo, price))


# Strip leading and trailing spaces of a string
exampleString = "    Hello people!      "
stripedExample = exampleString.strip()
print(stripedExample)


# Using find() and string slicing,
# extract the number at the end of the line below
# Convert the extracted value to a floating point number and print it

text = "X-DSPAM-Confidence:    0.8475"
colonPlace = text.find(":")
newText = text[colonPlace + 1 :]
newText = newText.strip()
newText = float(newText)
print(newText)

# One can combined all that code into one line like so...
# print(float(text[colonPlace + 1 :].strip()))
