# Zad. 1
# Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.

lista = [i for i in range(4, 100, 4)]

with open("dane.txt", "w") as file:
	file.writelines(str(l) + '\n' for l in lista)

# Zad. 2
# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli.

with open("dane.txt", "r") as file:
	print(file.read())
# Zad. 3
# Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.

with open('linijki.txt', "w+") as file:
	file.write("""Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with
desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.""")

with open("linijki.txt", "r") as file:
	print(file.read())


# Zad. 4
#
# Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
#
# nazwa_produktu, ilosc, jednostka_miary, cena_jed oraz metody:
# konstruktor – który nadaje wartości
# wyświetl_produkt() – drukuje informacje o produkcie na ekranie
# ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
# ile_kosztuje() – oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2
class NaZakupy:
	nazwa_produktu = None
	ilosc = None
	jednostka_miary = None
	cena_jed = None

	def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
		self.nazwa_produktu = nazwa_produktu
		self.ilosc = ilosc
		self.jednostka_miary = jednostka_miary
		self.cena_jed = cena_jed

	def wyswietl_produkt(self):
		print("""Nazwa produktu: {}
Ilość: {}
Jednostka miary: {}
Cena: {}""".format(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed))

	def ile_produktu(self):
		return "{} {}".format(self.ilosc, self.jednostka_miary)

	def ile_kosztuje(self):
		return float(self.ilosc) * float(self.cena_jed)


produkt = NaZakupy(nazwa_produktu="Ziemniaki", ilosc=3, jednostka_miary="kg", cena_jed=10)

produkt.wyswietl_produkt()
print(produkt.ile_produktu())
print(produkt.ile_kosztuje())


# Zad. 5
#
# Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
#
# wyświetl_dane – drukuje elementy na ekran
# pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
# pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
# policz_sume – liczy sume elementow
# policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.
class Ciag:
	ciagi = []
	a1 = None
	n = None
	r = None

	def wyswietl_dane(self):
		for ciag in self.ciagi:
			print(ciag, end="\t")
		print('')

	def pobierz_elementy(self):
		ciag = int(input("Podaj liczbe: "))

		self.ciagi.append(ciag)

	def pobierz_parametry(self):
		self.a1 = int(input("Podaj a1: "))
		self.n = int(input("Podaj n: "))
		self.r = int(input("Podaj r: "))

	def policz_sume(self):
		return sum(self.ciagi)

	def policz_elementy(self):
		if self.a1 is not None and self.r is not None:
			return len(self.ciagi)

ciag = Ciag()
ciag.pobierz_elementy()
ciag.pobierz_parametry()
print(ciag.policz_sume())
print(ciag.policz_elementy())
ciag.wyswietl_dane()

# Zad. 6
#
# Utwórz klasę Slowa, która będzie zarządzać różnymi grami słownymi. Klasa powinna przechowywać przynajmniej dwa słowa i metody:
#
# sprawdz_czy_palindrom – metoda sprawdza czy dany wyraz jest palindromem (czytany od początku czy wspak jest taki sam np. kajak)
# sprawdz_czy_metagramy – metoda sprawdza czy wyrazy różnią się jedną litera a poza tym są takie same np. mata, tata
# sprawdz_czy_anagramy – metoda sprawdza czy wyrazy maja ten sam zestaw liter. Np. mata i tama
# wyświetl_wyrazy – wyświetla podane wyrazy
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.

class Slowa:
	first_word = None
	second_word = None

	def __init__(self, first_word, second_word):
		self.first_word = first_word
		self.second_word = second_word

	def sprawdz_czy_palindrom(self):
		i = 0
		j = len(self.second_word) - 1

		while i < j:
			if self.first_word[i] != self.second_word[j]:
				return False

			i += 1
			j -= 1

		return True

	def sprawdz_czy_metagramy(self):
		min_length = min(len(self.first_word), len(self.second_word))
		max_length = max(len(self.first_word), len(self.second_word))

		difference_count = 0
		for i in range(min_length):
			if self.first_word[i] != self.second_word[i]:
				difference_count += 1

		difference_count += max_length - min_length

		if difference_count == 1:
			return True

		return False

	def sprawdz_czy_anagramy(self):
		first_list = list(self.first_word)
		second_list = list(self.second_word)

		print(first_list)

		if sorted(first_list) == sorted(second_list):
			return True

		return False

	def wyswietl_wyrazy(self):
		print("{}, {}".format(self.first_word, self.second_word))


slowa = Slowa(first_word="mata", second_word="atma")
print(slowa.sprawdz_czy_anagramy())
print(slowa.sprawdz_czy_metagramy())
print(slowa.sprawdz_czy_palindrom())


# Zad. 7
#
# Stwórz klasę Robot, która będzie sterować ruchami robota. Klasa powinna przechowywać współrzędne x, y, krok (stała wartość kroku dla robota),
# i powinna mieć następujące metody:
#
# konstruktor – który nadaje wartość dla x, y i krok
# idz_w_gore(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_dol(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_lewo(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_prawo(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne robota

class Robot:
	x = None
	y = None
	krok = None

	def __init__(self, x, y, krok=1):
		self.x = x
		self.y = y
		self.krok = krok

	def idz_w_gore(self, ile_krokow):
		self.y += ile_krokow * self.krok

	def idz_w_dol(self, ile_krokow):
		self.y -= ile_krokow * self.krok

	def idz_w_lewo(self, ile_krokow):
		self.x -= ile_krokow * self.krok

	def idz_w_prawo(self, ile_krokow):
		self.x += ile_krokow * self.krok

	def pokaz_gdzie_jestes(self):
		print("x: {}, y: {}".format(self.x, self.y))

	def __del__(self):
		print('--niszczenie--')


robot = Robot(x=5, y=5)
robot.idz_w_gore(ile_krokow=1)
robot.idz_w_dol(ile_krokow=2)
robot.idz_w_lewo(ile_krokow=3)
robot.idz_w_prawo(ile_krokow=4)
robot.pokaz_gdzie_jestes()

# Zad. 8
#
# Do klasy z wybranego poprzedniego zadania dołącz funkcję niszczenia obiektu.