import re
from Classes.Moneyline import PremierLeague

def BarstoolParser():
    file = open("data/PLOddsBarstool.txt")
    lines = file.readlines()
    index = 0
    current = 0
    naughtindex = []
    moneylineList = []

    for i in lines:
        if current + 4 < index and re.search("^([+]|[-])", i) != None:
            current = index
            naughtindex.append(index)
        index += 1
        
    for i in naughtindex:
        moneyline = PremierLeague(
            lines[i-1][:-1], 
            lines[i+1][:-1],
            lines[i][:-1], 
            lines[i+2][:-1], 
            lines[i+4][:-1])
        
        moneylineList.append(moneyline)

    return moneylineList
        