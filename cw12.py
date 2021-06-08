from lxml import html
import requests
from bs4 import BeautifulSoup
import urllib3
import pandas as pd
import json

header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}


# Zadanie 1
# Ze strony https://boardgamegeek.com pobierz linki (znajdź odpowiednie atrybuty) z sekcji 'The Hotness'. Wyświetl te linki.
def zadanie1():
	url = "https://api.geekdo.com/api/hotness?geeksite=boardgame&objecttype=thing&showcount=50"

	data = requests.get(url, headers=header)

	for d in data.json()['items']:
		print("https://boardgamegeek.com{}".format(d['href']))

# zadanie1()

def zadanie2():
	from lxml import html
	import requests

	url = "https://boardgamegeek.com/browse/boardgame"
	data = requests.get(url)

	page = html.fromstring(data.text)
	# tabela z grami wszechczasów (tylko pierwsza strona !), pobrana za pomocą XPath
	xpath = '//*[@id="collection"]//*[@class="table-responsive"]'
	# można pobierać elementy dokumentu również poprzez funkcje pakietu lxml po id lub klasie
	table_div = page.get_element_by_id('collection')

	# w dowolnym momencie na elemencie ponownie możemy pobrać elementy przez XPath, najważniejsza jest wiedza o drzewie DOM dokumentu w celu określenia odpowiedniej ścieżki względnej lub bezwzględnej
	# należy pamiętać (lub sprawdzić) to, że zostanie zwrócona lista odnalezionych elementów dokumentu, stąd index [0] aby zwrócić bezpośrednio ten element a nie całą listę
	table = table_div.xpath('./*[@class="table-responsive"]/table')[0]
	# print(table)

	# kolejna informacja jest taka, że większość (ale nie wszystkie) nagłówków jest w formie łącza (znacznik <a>), trzeba więc wyłuskać z niego tekst
	headers = [label for label in table.xpath('.//td')]
	labels = []
	for header in headers:
		anchor = header.xpath('./a/text()')
		if len(anchor) > 0:
			# znowu anchor to lista, pozbywamy się znaków niedrukowalnych
			labels.append(anchor[0].strip())
		else:
			# trzeba pozbyć się znaków niedrukowalnych
			labels.append(header.text.strip())
	print(labels)
# zadanie2()

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
