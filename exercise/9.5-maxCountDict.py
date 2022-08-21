# 9.4 Write a program to read through  mbox-short.txt
# figure who has sent the greatest number of messages.
# The program looks for 'From ' lines and
# takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
# Sample Output :
#   ...
#   cwen@iupui.edu 5

name = input("Enter file:")
if len(name) < 1:
    name = "samples\mboxShort.txt"

nameList = list()
counts = dict()

try:
    handle = open(name, 'r')
    for line in handle:
        if not line.startswith('From '):
            continue
        else:
            newList = line.split()
            nameList.append(newList[1])
    # print("\nNameList = ", nameList)

    for name in nameList:
        counts[name] = counts.get(name, 0) + 1
    # print("\nCount = ", counts)

    nameCount = None
    theName = None
    for name, count in counts.items():
        if nameCount is None or count > nameCount:
            theName = name
            nameCount = count

    print(theName, nameCount)

except:
    print("Sorry, that is not a valid file name or the file cannot be opened.")
    quit
