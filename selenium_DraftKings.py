# Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Variables for each websites PL odds
DraftKings = "https://sportsbook.draftkings.com/leagues/soccer/england---premier-league"
Fanduel = "https://sportsbook.fanduel.com/soccer?tab=epl"
Bet365 = "https://www.oh.bet365.com/?_h=XG4D8hz5aYaLFAgHTDdlYA%3D%3D#/AC/B1/C1/D1002/E76169570/G40/H^1/"
BetMGM = "https://sports.oh.betmgm.com/en/sports/soccer-4/betting/england-14"
PointsBet = "https://oh.pointsbet.com/sports/soccer/English-Premier-League/138839"

# Open Draftkings, had to use an "Options" workaround online as it refused to stay open
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(DraftKings)
# Verification that we're on the correct page
print(driver.title)

# Action of printing each bit of text on the page into individual lines
webpage = driver.find_element("tag name", "html")
print(webpage.text)

# Action of creating a new text file and writing what the terminal prints inside
Parsefile = open('DraftKingsPLOdds.txt', 'w')
Parsefile.writelines(webpage.text)
