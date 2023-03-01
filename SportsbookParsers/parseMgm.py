import re

file = open("PLOddsBetMGM.txt")
lines = file.readlines()
index = 0
current = 0
naughtindex = []

for i in lines:
    if current + 2 < index and re.search("2.5", i) != None:
        current = index
        naughtindex.append(index)
        
    index += 1

for i in naughtindex:
    print("{0} vs {1}\n{0} Wins: {2}, Draw: {3}, {1} Wins: {4}\n\n".format(
        lines[i-5][:-1],
        lines[i-4][:-1], 
        lines[i-3][:-1], 
        lines[i-2][:-1], 
        lines[i-1][:-1]))