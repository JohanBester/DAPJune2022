# 10.2 Write a program to ...
# read through the mbox-short.txt and
# figure out the distribution by hour of the day,for each messages.
# You can pull the hour out from the 'From ' line by
#  - finding the time and then
#  - splitting the string a second time using a colon.
#
# EG:- From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 200
#
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.
#
# Sample OutPut:
# ...
#   04 3
#   06 1
#   07 1
#   09 2
#   10 3
#   11 6
#   14 1
#   15 2
#   16 4
#   17 2
#   18 1
#   19 1

name = input("Enter file:")
if len(name) < 1:
    name = "samples\mboxShort.txt"

try:
    handle = open(name, 'r')
    timeList = list()
    hourList = list()
    counts = dict()

    for line in handle:
        if not line.startswith('From '):
            continue
        else:
            lst = line.split()
            timeList.append(lst[5])
    # print("\ntimeList", timeList)

    for time in timeList:
        lst = time.split(":")
        hourList.append(lst[0])
    # print("\nhourList", hourList)

    for hour in hourList:
        counts[hour] = counts.get(hour, 0) + 1
    # print("\nCounts", counts)

    # finalList = sorted(counts.items())
    # print("\nfinalList", finalList)

    for key, val in sorted(counts.items()):
        print(key, val)

except:
    print("Sorry, that is not a valid file name or the file cannot be opened.")
    quit
