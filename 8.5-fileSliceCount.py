# 8.5 Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# You will parse the From line using split()
# and print out the second word in the line
# (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# Look at the sample output to see how to print the count.
# Sample Output :
#   ...
#   cwen@iupui.edu
#   cwen@iupui.edu
#   There were 27 lines in the file with From as the first word

# You can download sample data at http://www.py4e.com/code3/mbox-short.txt

# file found locally at samples\mboxShort.txt

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "samples\mboxShort.txt"
count = 0
try:
    fh = open(fname, 'r')

    for line in fh:
        if not line.startswith('From '):
            continue
        else:
            count = count + 1
            newList = line.split()
            print(newList[1])

except:
    print("Sorry, that is not a valid file name or the file cannot be opened.")
    quit

print("There were", count, "lines in the file with From as the first word")
