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
        return

class PremierLeague(Moneyline):
    def __init__(self, homeTeam, awayTeam, homeWin, awayWin, draw) -> None:
        super().__init__(homeTeam, awayTeam, homeWin, awayWin)
        self.draw = draw