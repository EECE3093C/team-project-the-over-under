import re

file = open("C:\\Users\\15136\Documents\\fanduelhtml.txt")
lines = file.readlines()
index = 0
current = 0
naughtindex = []
for i in lines:
    if current + 2 < index and re.search("^([+]|[-])", i) != None:
        current = index
        naughtindex.append(index)
    index += 1

for i in naughtindex:
    print("{0} vs {1}\n{0} Wins: {2}, Draw: {3}, {1} Wins: {4}\n\n".format(
        lines[i-2][:-1],
        lines[i-1][:-1], 
        lines[i][:-1], 
        lines[i+1][:-1], 
        lines[i+2][:-1]))
        