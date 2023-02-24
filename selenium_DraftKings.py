# Imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



# Open Draftkings, had to use an "Options" workaround online as it refused to stay open
# using a regular PATH
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://sportsbook.draftkings.com/leagues/soccer/england---premier-league")
print(driver.title)
ready = 0
driver.maximize_window()
spans = driver.find_elements("tag name", "div")
divlist = []

webpage = driver.find_element("tag name", "html")
print(webpage.text)

Parsefile = open('DraftKingsPLOdds.txt', 'w')
Parsefile.writelines(webpage.text)
