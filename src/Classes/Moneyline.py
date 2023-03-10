class Moneyline:
    def __init__(self, homeTeam, awayTeam, homeWin, awayWin) -> None:
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.homeWin = homeWin
        self.awayWin = awayWin

    def getHomeTeam(self):
        return self.homeTeam
    
    def getAwayTeam(self):
        return self.awayTeam
    
    def getHomeWin(self):
        return self.homeWin
    
    def getAwayWin(self):
        return self.awayWin
    
    def setHomeWin(self, homeWin : int):
        self.homeWin = homeWin
    
    def setAwayWin(self, awayWin : int):
        self.awayWin = awayWin

class PremierLeague(Moneyline):
    def __init__(self, homeTeam, awayTeam, homeWin, awayWin, draw) -> None:
        super().__init__(homeTeam, awayTeam, homeWin, awayWin)
        self.draw = draw

    def getDraw(self):
        return self.draw
    
    def setDraw(self, draw : int):
        self.draw = draw