# Imports
from selenium import webdriver
import time

# Variables for each websites PL odds
DraftKings = "https://sportsbook.draftkings.com/leagues/soccer/england---premier-league"
Fanduel = "https://sportsbook.fanduel.com/soccer?tab=epl"
Barstool = "https://www.barstoolsportsbook.com/sports/football/england/premier_league"
BetMGM = "https://sports.oh.betmgm.com/en/sports/soccer-4/betting/england-14"
PointsBet = "https://oh.pointsbet.com/sports/soccer/English-Premier-League"

# Open Draftkings
# minor adjustments here to get rid of USB_device_handle_win error, and UniEncodeError 'charmap'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get(DraftKings)
time.sleep(10)

# Verification that we're on the correct page
# works perfectly, prints out entire page with moneylines
print(driver.title)

# Action of printing each bit of text on the page into individual lines
webpage = driver.find_element("tag name", "html")
print(webpage.text)

# Action of creating a new text file and writing what the terminal prints inside
Parsefile = open('DraftKingsPLOdds.txt', 'w')
Parsefile.writelines(webpage.text)


# Now we can run this on all 5 websites from one file
# Fanduel Scraping
driver.get(Fanduel)
time.sleep(10)
print(driver.title)

webpage = driver.find_element("tag name", "html")
print(webpage.text)

Parsefile = open('PLOddsFanDuel.txt', 'w')
Parsefile.writelines("FANDUEL PREMIER LEAGUE MONEYLINE ODDS \n")
Parsefile.writelines(webpage.text)


# Barstool Scraping
driver.get(Barstool)
time.sleep(10)
print(driver.title)

webpage = driver.find_element("tag name", "html")
print(webpage.text)

Parsefile = open('PLOddsBarstool.txt', 'w')
Parsefile.writelines("BARSTOOL PREMIER LEAGUE MONEYLINE ODDS \n")
Parsefile.writelines(webpage.text)


# BetMGM Scraping
driver.get(BetMGM)
time.sleep(10)
print(driver.title)

webpage = driver.find_element("tag name", "html")
print(webpage.text)

Parsefile = open('PLOddsBetMGM.txt', 'w')
Parsefile.writelines("BETMGM PREMIER LEAGUE MONEYLINE ODDS \n")
Parsefile.writelines(webpage.text)


# PointsBet Scraping
driver.get(PointsBet)
time.sleep(10)
print(driver.title)

webpage = driver.find_element("tag name", "html")
print(webpage.text)

Parsefile = open('PLOddsPointsBet.txt', 'w')
Parsefile.writelines("POINTSBET PREMIER LEAGUE MONEYLINE ODDS \n")
Parsefile.writelines(webpage.text)
driver.close()
