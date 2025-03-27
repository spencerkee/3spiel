import requests
from bs4 import BeautifulSoup
import ipdb

from selenium import webdriver
from selenium.webdriver import Safari

driver = Safari()

# https://boardgamegeek.com/boardgame/169786/scythe
# https://boardgamegeek.com/boardgame/169786/scythe/credits#boardgamefamily


# URL = "https://realpython.github.io/fake-jobs/"
URL = "https://boardgamegeek.com/boardgame/169786/scythe/credits"
# page = requests.get(URL)

# print(page.text)
# soup = BeautifulSoup(page.content, "html.parser")


# Find by ID
# results = soup.find(id="ResultsContainer")
# print(results.prettify())

# job_cards = results.find_all("div", class_="card-content")


def get_full_game_name(soup):
    pass


# import mechanicalsoup

# browser = mechanicalsoup.StatefulBrowser()
# browser.open(URL)
# browser.launch_browser()

driver.get(URL)
ipdb.set_trace()
pass
