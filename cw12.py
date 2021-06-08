from lxml import html
import requests
from bs4 import BeautifulSoup
import urllib3
import pandas as pd

header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}


# Zadanie 1
# Ze strony https://boardgamegeek.com pobierz linki (znajdź odpowiednie atrybuty) z sekcji 'The Hotness'. Wyświetl te linki.
def zadanie1():
	url = "https://boardgamegeek.com/hotness"

	data = requests.get(url, headers=header)
	# print html
	print(data.text)

	page = html.fromstring(data.text)


# 	Javascript not loaded

# zadanie1()

def zadanie4():
	url = "https://www.metacritic.com/browse/games/genre/metascore/strategy/pc?view=detailed"
	page = requests.get(url, headers=header)
	soup = BeautifulSoup(page.content, 'html.parser')

	popular_games = list()
	for clamp in soup.find_all(class_="clamp-list"):
		for idx, box in enumerate(clamp.find_all('tr')):
			if idx % 2 == 0:
				title = box.find('h3').text
				platform = box.find(class_='data').text.strip()
				release_date = box.find(class_="clamp-details").find_all('span')[2].text
				score = int(box.find(class_="metascore_w").text)
				popular_games.append([title, platform, release_date, score])
	df = pd.DataFrame(data=popular_games, columns=['Title', 'Platform', 'Release date', 'Score'])
	print(df)


# zadanie4()

def zadanie5():
	page_number = 0

	popular_games = list()
	while page_number != 10:
		url = "https://www.metacritic.com/browse/games/genre/metascore/strategy/pc?view=detailed&page={}".format(page_number)
		page = requests.get(url, headers=header)
		soup = BeautifulSoup(page.content, 'html.parser')

		for clamp in soup.find_all(class_="clamp-list"):
			for idx, box in enumerate(clamp.find_all('tr')):
				if idx % 2 == 0:
					title = box.find('h3').text
					platform = box.find(class_='data').text.strip()
					release_date = box.find(class_="clamp-details").find_all('span')[2].text
					score = int(box.find(class_="metascore_w").text)
					popular_games.append([title, platform, release_date, score])
		page_number += 1
	df = pd.DataFrame(data=popular_games, columns=['Title', 'Platform', 'Release date', 'Score'])
	print(df[df['Platform'] == 'PC'][:10])


# zadanie5()
