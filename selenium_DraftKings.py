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
# using a regular PATH
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(DraftKings)
print(driver.title)
ready = 0
driver.maximize_window()
spans = driver.find_elements("tag name", "div")
divlist = []

webpage = driver.find_element("tag name", "html")
print(webpage.text)

Parsefile = open('DraftKingsPLOdds.txt', 'w')
Parsefile.writelines(webpage.text)
