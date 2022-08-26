import re
numList = list()
for line in open("samples\\regex_sum_1613403.txt", 'r'):
    for num in re.findall('([0-9]+)', line.rstrip()):
        numList.append(int(num))
print(sum(numList))


# Old Code
# name = "samples\\regex_sum_42.txt"
# name = "samples\\regex_sum_1613403.txt"
# fh = open(name, 'r')
# for line in fh:
# line = line.rstrip()
# numbers = re.findall('([0-9]+)', line)
# for num in numbers:
# numList.append(int(num))
# print(sum(numList))
