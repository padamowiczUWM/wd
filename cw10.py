import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

imiona_xlsx = pd.ExcelFile('datasets/imiona.xlsx')
imiona = pd.read_excel(imiona_xlsx)
zamowienia = pd.read_csv('datasets/zamowienia.csv', delimiter=';')


# Zadanie 1
# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20]. Dodaj etykietę do linii wykresu i
# wyświetl legendę. Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz
# (1, długość wektora x).
def zadanie1():
	x = np.linspace(0, 20)
	plt.axis([0, 20, 0, 1])
	plt.plot(x, 1 / x, label='f(x) = 1/x')
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.legend()
	plt.show()


# zadanie1()

# Zadanie 2
# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.
def zadanie2():
	x = np.linspace(0, 20, 21)
	plt.axis([0, 20, 0, 1])
	plt.plot(x, 1 / x, "g>:", label='f(x) = 1/x')
	plt.xlabel('x')
	plt.title('Wykres funkcji f(x) dla x [1,20]')
	plt.ylabel('f(x)')
	plt.legend()
	plt.show()


# zadanie2()

# Zadanie 3
# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1.
# Dodaj etykiety i legendę do wykresu.
def zadanie3():
	x = np.arange(0, 30, 0.1)
	s = np.sin(x)
	c = np.cos(x)
	plt.plot(x, s, label='sin(x)')
	plt.plot(x, c, label='cos(x)')

	# etykiety osi
	plt.xlabel('x')
	plt.ylabel('sin(x) i cos(x)')

	# tytuł wykresu
	plt.title("Wykres sin(x) i cos(x)")

	# umieszczamy legendę na wykresie
	plt.legend()

	plt.show()


# zadanie3()


# Zadanie 4
# Dodaj drugi wykres funkcji sinus do zadania 3 i zmodyfikuj parametry funkcji, tak aby osiągnąć efekt podobny do tego na poniższym zrzucie ekranu.
def zadanie4():
	x = np.arange(0, 30, 0.1)
	s = np.sin(x)
	c = np.sin(x)
	plt.plot(x, 2 + s, x, -c, label='sin(x)')

	# etykiety osi
	plt.xlabel('x')
	plt.ylabel('sin(x)')

	# tytuł wykresu
	plt.title("Wykres sin(x), sin(x)")

	# umieszczamy legendę na wykresie
	plt.legend(loc="center left")

	plt.show()


# zadanie4()

# Zadanie 5
# Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris) wygeneruj wykres punktowy, gdzie wektor x to wartość
# ‘sepal length’ a y to ‘sepal width’, dodaj paletę kolorów c na przykładzie listingu 6 a parametr s niech będzie wartością absolutną
# z różnicy wartości poszczególnych elementów wektorów x oraz y.
def zadanie5():
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
	color = np.random.randint(0, 50, len(data))

	s = []

	for i in range(len(data)):
		s.append(math.fabs(data.iloc[i]['sepal length in cm'] - data.iloc[i]['sepal width in cm']))

	plt.scatter('sepal length in cm', 'sepal width in cm', c=color, s=s, data=data)
	plt.annotate('niezwykła wartość',
				 xy=(5.1, 3.5), xycoords='data',
				 xytext=(-15, 25), textcoords='offset points',
				 arrowprops=dict(facecolor='black', shrink=0.05),
				 horizontalalignment='right', verticalalignment='top')
	plt.show()


zadanie5()


# Zadanie 6
# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8.
# Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny).
# Dodaj do wykresów stosowne etykiety. Poustawiaj różne kolory dla wykresów.
# 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie.
# 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla mężczyzn dla każdego roku z osobna.
# Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.
# 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.
def zadanie6():
	narodziny = imiona.groupby(['Plec']).agg({'Liczba': 'sum'})
	narodziny_rok_kobieta = imiona[imiona['Plec'] == 'K'].groupby(['Rok']).sum()
	narodziny_rok_mezczyzna = imiona[imiona['Plec'] == 'M'].groupby(['Rok']).sum()
	narodziny_rok = imiona.groupby(['Rok']).agg({'Liczba': 'sum'})

	plt.subplot(1, 3, 1)
	plt.bar(x=['K', 'M'], height='Liczba', data=narodziny)
	plt.ylabel('Ilość narodzin')
	plt.xlabel('Płeć')
	plt.title('Ilość narodzonych dziewczynek i chłopców')

	plt.subplot(1, 3, 2)
	plt.plot(narodziny_rok_kobieta, label="Kobieta")
	plt.plot(narodziny_rok_mezczyzna, label="Mężczyzna")
	plt.xlabel('Rok')
	plt.ylabel('Ilość')
	plt.title('Ilość urodzonych dla kazdego roku z osobna')
	plt.legend()

	plt.subplot(1, 3, 3)
	plt.bar(x=imiona['Rok'].unique(), height='Liczba', data=narodziny_rok)
	plt.xlabel('Rok')
	plt.ylabel('Ilość')
	plt.title('Suma urodzonych dzieci w każdym roku')

	plt.show()


# zadanie6()

# Zadanie 7
#
# Korzystając z tutoriala pod adresem
# https://towardsdatascience.com/matplotlib-tutorial-learn-basics-of-pythons-powerful-plotting-library-b5d1b8f67596 lub innego
# zmodyfikuj wykres 2 z zadania 6 tak, aby zamiast wykresu liniowego przedstawiał wykres łupkowy skumulowany
# (czyli jeden słupek dla kobiet i mężczyzn, ale składający się z dwóch „nałożonych” na siebie słupków).
def zadanie7():
	narodziny_rok_kobieta = imiona[imiona['Plec'] == 'K'].groupby(['Rok']).sum()
	narodziny_rok_mezczyzna = imiona[imiona['Plec'] == 'M'].groupby(['Rok']).sum()
	print(imiona.groupby(['Rok']).sum())
	plt.bar(imiona['Rok'].unique(), height='Liczba', data=narodziny_rok_kobieta, color="blue", label="Kobieta")
	plt.bar(imiona['Rok'].unique(), height='Liczba', data=narodziny_rok_mezczyzna, color="red", label="Mężczyzna",
			bottom=narodziny_rok_kobieta['Liczba'])
	plt.xticks(imiona['Rok'].unique())
	plt.xlabel('Rok')
	plt.ylabel('Ilość')
	plt.title('Ilość urodzonych dla kazdego roku z osobna')
	plt.annotate('największa wartość',
				 xy=(2009, 450692), xycoords='data',
				 xytext=(-15, 25), textcoords='offset points',
				 arrowprops=dict(facecolor='black', shrink=0.05),
				 horizontalalignment='right', verticalalignment='top')
	plt.legend()
	plt.show()


# zadanie7()


# Zadanie 8
# Napisz funkcję, która losowo rzuca dwiema kostkami k6 n razy. Wynik rzutów zapisywany jest w postaci listy sum oczek
# z tych dwóch kostek. Np. rzucaj(6) generuje 6 rzutów kostkami i zwraca wektor 6 sum oczek każdego rzutu. Po zakończeniu
# funkcji wyświetlaj histogram sumy rzutów. Dodaj stosowne etykiety do wykresu.
def zadanie8():
	def rzucaj(n):
		k1 = np.random.randint(1, 7, n)
		return [i + np.random.randint(1, 7) for i in k1]

	plt.hist(rzucaj(6), bins=12, facecolor='g', alpha=0.75, density=True)
	plt.xlabel('Suma oczek')
	plt.ylabel('Prawdopodobieństwo')
	plt.title('Dwa rzuty kostką')
	# wyświatlanie siatki
	plt.grid(True)
	plt.show()


# zadanie8()

# Zadanie 9
# Korzystając z pliku zamówienia.csv (Pandas) policz sumy zamówień dla każdego przedawcy i wyświetl wykres kołowy z
# procentowym udziałem każdego sprzedawcy w ogólnej sumie zamówień. Poszukaj w Internecie jak dodać cień do takiego
# wykresu i jak działa atrybut ‘explode’ tego wykresu. Przetestuj ten atrybut na wykresie.
def zadanie9():
	utarg = zamowienia.groupby('Sprzedawca').sum('Utarg')

	wedges, texts, autotexts = plt.pie(utarg['Utarg'], labels=zamowienia['Sprzedawca'].unique(),
									   autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"),
									   shadow=True, explode=np.random.random(9))
	plt.setp(autotexts, size=14, weight="bold")
	plt.title("Pierwsza wersja wykresu")
	plt.legend(title='Zawodnicy')
	plt.show()

# zadanie9()

# Zadanie 10
# Poszukaj w bibliotece wykresów (https://matplotlib.org/gallery/index.html) przykładów z adnotacjami
# (annotating plots) na wykresach i dodaj adnotacje do dwóch wybranych stworzonych wcześniej wykresów.
