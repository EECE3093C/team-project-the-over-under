import SportsbookParsers.BarstoolParser as BarstoolParser

for item in BarstoolParser.BarstoolParser():
    print(item.getHomeTeam(), "v.", item.getAwayTeam())