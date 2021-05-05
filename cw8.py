import pandas as pd

# Zadanie 1
# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx
def zadanie1():
	xlsx = pd.ExcelFile('datasets/imiona.xlsx')
	df = pd.read_excel(xlsx)

	return df

# zadanie1()

# Zadanie 2
#
# Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):
#
# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# tylko rekordy gdzie nadane imię jest takie jak Twoje
# sumę wszystkich urodzonych dzieci w całym danym okresie,
# sumę dzieci urodzonych w latach 2000-2005
# sumę urodzonych chłopców i dziewczynek,
# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,
# Zadanie 3

def zadanie2():
	df = zadanie1()

	print(df[df['Liczba'] > 1000])
	print(df[df['Imie'] == 'PATRYK'])
	print(df.groupby(['Rok']).agg({'Liczba': ['sum']}))
	print(df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)].groupby(['Rok']).agg({'Liczba':['sum']}))
	print(df.groupby(['Plec']).agg({'Liczba':['sum']}))

# zadanie2()

# Zadanie 3
#
# Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:
#
# listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
# 5 najwyższych wartości zamówień
# ilość zamówień złożonych przez każdego sprzedawcę
# sumę zamówień dla każdego kraju
# sumę zamówień dla roku 2005, dla sprzedawców z Polski
# średnią kwotę zamówienia w 2004 roku,
# zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
def zadanie3():
	df = pd.read_csv('datasets/zamowienia.csv', sep=';')
	print(df['Sprzedawca'].unique())
	print(df.sort_values(by="Utarg", ascending=False).iloc[0:5])
	print(df.groupby(['Sprzedawca']).size())
	print(df.groupby(['Kraj']).size())

	order_2004 = (df['Data zamowienia'] > '2004-01-01') & (df['Data zamowienia'] < '2004-12-31')
	order_2005 = ((df['Data zamowienia'] > '2005-01-01') & (df['Data zamowienia'] < '2005-12-31'))

	print(df[order_2005 & (df['Kraj'] == 'Polska')].size)
	print(df[order_2004]['Utarg'].mean())

	df[order_2004].to_csv('zamówienia_2004.csv', header=None, index=False)
	df[order_2005].to_csv('zamówienia_2005.csv', header=None, index=False)

# zadanie3()