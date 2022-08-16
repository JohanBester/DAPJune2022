# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list
# and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.

# You can download the sample data at http://www.py4e.com/code3/romeo.txt
# Stored locally at ... C:\Users\jbest\OneDrive\WORK RELATED\03_SAVVY Files\2022_June_DAP\Coursera_Python_CodeSamples\romeo.txt

# # Use romeo.txt as the file name

fname = input("Enter file name: ")
wordList = []
try:
    fh = open(fname, 'r')
    for line in fh:
        line = line.rstrip()
        words = line.split()
        for wrd in words:
            if wrd in wordList:
                continue
            else:
                wordList.append(wrd)

except:
    print("Sorry, that is not a valid file name or the file cannot be opened.")
    quit

wordList.sort()
print(wordList)
