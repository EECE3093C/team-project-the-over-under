# Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



# Open Draftkings, had to use an "Options" workaround online as it refused to stay open
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://sportsbook.draftkings.com/leagues/soccer/england---premier-league")
# Verification that we're on the correct page
print(driver.title)

# Action of printing each bit of text on the page into individual lines
webpage = driver.find_element("tag name", "html")
print(webpage.text)

# Action of creating a new text file and writing what the terminal prints inside
Parsefile = open('DraftKingsPLOdds.txt', 'w')
Parsefile.writelines(webpage.text)
