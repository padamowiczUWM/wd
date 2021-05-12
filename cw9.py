import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

imiona_xlsx = pd.ExcelFile('datasets/imiona.xlsx')
imiona = pd.read_excel(imiona_xlsx)
zamowienia = pd.read_csv('datasets/zamowienia.csv', delimiter=';')


# Zadanie 1
# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.
def zadanie1():
	df = imiona.groupby('Rok').agg({'Liczba': 'sum'})
	df.plot()
	plt.show()


# zadanie1()

# Zadanie 2
# Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.
def zadanie2():
	df = imiona.groupby(['Plec']).agg({'Liczba': ['sum']})
	wykres = df.plot.bar()
	wykres.set_ylabel('Liczba urodzonych')
	wykres.set_xlabel('Płeć')
	wykres.legend()
	plt.show()


# zadanie2()

# Zadanie 3
# Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.
def zadanie3():
	grupa = imiona[imiona['Rok'] > 2012].groupby(['Plec']).agg({'Liczba': ['sum']})
	# wykres kołowy z wartościami procentowymi sformatowanymi z dokładnością do 2 miejsc po przecinku
	# figsize ustawia wielkość wykresu w calach, domyślnie [6.4, 4.8].
	wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
	plt.title('Ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach')
	plt.show()


# zadanie3()

# Zadanie 4
# Z repozytorium UCI (http://archive.ics.uci.edu/ml/index.php) pobierz dataset Iris i za pomocą wykresu punktowego
# (scattered) wyświetl wartość 2 wybranych cech tego datasetu. Dla każdego rodzaju kwiatu użyj innego koloru na wykresie.
# Przykład można znaleźć w galerii wykresów biblioteki matplotlib - link w materiałach matplotlib.
def zadanie4():
	data = pd.read_csv(
		'datasets/iris.data',
		delimiter=',',
		names=[
			'sepal length in cm',
			'sepal width in cm',
			'petal length in cm',
			'petal width in cm',
			'class'
		]
	)

	colors = []
	for _class in data['class']:
		if _class == 'Iris-versicolor':
			colors.append('b')
		elif _class == 'Iris-setosa':
			colors.append('r')
		else:
			colors.append('g')

	data.plot.scatter(x='sepal length in cm', y='petal length in cm', c=colors)
	plt.show()


zadanie4()


# Zadanie 5
# Wyświetl za pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór danych zamówienia.csv).
def zadanie5():
	df = zamowienia.groupby(['Sprzedawca'])['idZamowienia'].count()
	wykres = df.plot.bar()
	wykres.set_ylabel('Ilość zamówień')
	wykres.set_xlabel('Sprzedawca')
	wykres.legend()
	plt.show()

# zadanie5()
