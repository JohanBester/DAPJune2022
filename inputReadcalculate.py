# 7.2 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and
# extract the floating point values from each of the lines
# and compute the average of those values
# and produce an output as shown below.
# "Average spam confidence: 0.7507185185185187"
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# Stored locally at ... C:\Users\jbest\OneDrive\WORK RELATED\03_SAVVY Files\2022_June_DAP\Coursera_Python\mbox-short.txt

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
count = 0
sNum = avgSpam = float(0.0)

try:
    fh = open(fname, 'r')
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        else:
            count = count + 1
            line = line.rstrip()
            colonPlace = line.find(":")
            newText = line[colonPlace+1:].lstrip()
            num = float(newText)
            sNum = sNum + num

    avgSpam = (sNum / count)
    print("Average spam confidence:", avgSpam)

except:
    print("Sorry, that is not a valid file name or the file cannot be opened.")
    quit
