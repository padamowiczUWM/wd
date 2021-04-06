# Zad. 1
#
# Stwórz 3 klasy: Material, Ubrania, Sweter. Klasa: Material
#
# Atrybuty:
#
# rodzaj,
# długość
# szerokość
# Metody:
#
# konstruktor
# wyświetl_nazwę
# Klasa: Ubrania
#
# Atrybuty:
#
# rozmiar
# kolor
# dla_kogo
# Metody:
#
# wyświetl_dane – do wyświetlania informacji o ubraniu
# klasa: Sweter
#
# Atrybuty:
#
# rodzaj_swetra – np. Rozpinany, z golfem itd.
# Metody:
#
# wyświetl_dane
# Ubrania dziedziczą po klasie Materiał, a Swetry po klasie Ubrania. Stwórz kilka instancji obiektów i sprawdź, które metody można wykorzystać.
class Material:
	def __init__(self, rodzaj, długość, szerokość):
		self.rodzaj = rodzaj
		self.długość = długość
		self.szerokość = szerokość

	def wyświetl_nazwę(self):
		print(self.rodzaj)


class Ubrania(Material):
	rozmiar = None
	kolor = None
	dla_kogo = None

	def wyświetl_dane(self):
		print("Rozmiar: {}\nKolor: {}\nDla kogo: {}\nRodzaj: {}\nDługość {}\nSzerokość: {}".format(
			self.rozmiar,
			self.kolor,
			self.dla_kogo,
			self.rodzaj,
			self.długość,
			self.szerokość))


class Sweter(Ubrania):
	rodzaj_swetra = "Rozpinany"

	def wyświetl_dane(self):
		return "Rodzaj swetra: {}".format(self.rodzaj_swetra)


material = Material(rodzaj="bawełna", długość=24, szerokość=25)
material.wyświetl_nazwę()
bluza = Ubrania(rodzaj="poliester", długość=26, szerokość=50)
bluza.rozmiar = "S"
bluza.kolor = "Czerwony"
bluza.dla_kogo = "Mężczyzna"
bluza.wyświetl_dane()
bluza.wyświetl_nazwę()
sweter = Sweter(rodzaj="poliester", długość=26, szerokość=50)
sweter.rozmiar = "S"
sweter.kolor = "Zielony"
sweter.dla_kogo = "Kobieta"
sweter.wyświetl_nazwę()
sweter.wyświetl_dane()


# Zad. 2
#
# Przeciąż metodę __add__() dla klasy Kwadrat, która będzie zwracała instancje klasy Kwadrat
# o nowym boku, będącym sumą boków dodawanych do siebie kwadratów.
class Ksztalty:
	# definicja konstruktora
	def __init__(self, x, y):
		# deklarujemy atrybuty
		# self wskazuje że chodzi o zmienne właśnie definiowanej klasy
		self.x = x
		self.y = y
		self.opis = "To będzie klasa dla ogólnych kształtów"

	def pole(self):
		return self.x * self.y

	def obwod(self):
		return 2 * self.x + 2 * self.y

	def dodaj_opis(self, text):
		self.opis = text

	def skalowanie(self, czynnik):
		self.x = self.x * czynnik
		self.x = self.y * czynnik


class Kwadrat(Ksztalty):
	def __init__(self, x):
		self.x = x
		self.y = x

	def __str__(self):
		return 'Kwadrat o boku {}'.format(self.x)

	def __add__(self, kwadrat):
		if isinstance(kwadrat, Kwadrat):
			return Kwadrat(self.x + kwadrat.x)

		return None

	def __ge__(self, kwadrat):
		if isinstance(kwadrat, Kwadrat):
			if self.x >= kwadrat.x:
				return True

			return False

		return None

	def __gt__(self, kwadrat):
		if isinstance(kwadrat, Kwadrat):
			if self.x > kwadrat.x:
				return True

			return False

		return None

	def __le__(self, kwadrat):
		if isinstance(kwadrat, Kwadrat):
			if self.x <= kwadrat.x:
				return True

			return False

		return None

	def __lt__(self, kwadrat):
		if isinstance(kwadrat, Kwadrat):
			if self.x < kwadrat.x:
				return True

			return False

		return None


kw = Kwadrat(5)
print(kw + Kwadrat(5))
print(kw >= Kwadrat(5))
print(kw > Kwadrat(5))
print(kw <= Kwadrat(5))
print(kw < Kwadrat(5))


# Zad. 3
#
# Poczytaj o metodach __ge__, __gt__, __le__, __lt__, przeciąż je i spróbuj wykorzystać
# w instrukcji warunkowej do porównania dwóch instancji obiektów klasy Kwadrat.

# Zad. 4
#
# Korzystając z powyższego kodu stwórz kilka instancji klasy Point i spróbuj odwołać się do zmiennej counter z
# poziomu różnych instancji, porównując jej wartość dla każdej z nich oraz spróbuj zmienić jej wartość.
#
# Ciekawostką jest to, że możemy stworzyć „pustą” klasę tylko po to, żeby przechować wartość wielu zmiennych
# w pojedynczej referencji, coś jak struktura w języku C.

class Point:
	counter = []

	def __init__(self, x=0, y=0):
		"""Konstruktor punktu."""
		self.x = x
		self.y = y

	def update(self, n):
		self.counter.append(n)


p1 = Point(0, 0)
p2 = Point(1, 1)
p3 = Point(2, 2)

print(p1.counter)
p1.update(1)
print(p1.counter)
print(p3.counter)
p2.counter = [5]
print(p2.counter)
print(p3.counter)


# Zad. 5
# Za pomocą funkcji isinstance() oraz issubclass() sprawdź wynik dla instancji obiektu Pracownik
# oraz Menadzer dla klas Osoba, Pracownik i Manadzer.
class Osoba:
	def __init__(self, imie, nazwisko):
		self.imie = imie
		self.nazwisko = nazwisko

	def przedstaw_sie(self):
		return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):
	def __init__(self, imie, nazwisko, pensja):
		Osoba.__init__(self, imie, nazwisko)
		# lub
		# super().__init__(imie, nazwisko)
		self.pensja = pensja

	def przedstaw_sie(self):
		return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):
	def przedstaw_sie(self):
		return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)
print(isinstance(jozek, Osoba))
print(isinstance(jozek, Pracownik))
print(isinstance(jozek, Menadzer))
print(isinstance(adrian, Osoba))
print(isinstance(adrian, Pracownik))
print(isinstance(adrian, Menadzer))

print(issubclass(Pracownik, Osoba))
print(issubclass(Pracownik, Pracownik))
print(issubclass(Pracownik, Menadzer))
print(issubclass(Menadzer, Osoba))
print(issubclass(Menadzer, Pracownik))
print(issubclass(Menadzer, Menadzer))


# Zad. 6
# Przetestuj powyższy iterator na kilku różnych kolekcjach.
class Wspak:
	"""Iterator zwracający wartości w odwróconym porządku"""

	def __init__(self, data):
		self.data = data
		self.index = len(data)

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index -= 1
		return self.data[self.index]


print('-------')
it = Wspak('kot')
print(next(it))
print(next(it))
print(next(it))

print('-------')
it = Wspak('pies')
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# Zad. 7
# Napisz własny iterator, który będzie zwracał tylko elementy z parzystych indeksów przekazanej kolekcji.
class Parzyste:
	def __init__(self, text):
		self.text = text
		self.index = 0

	def __iter__(self):
		return self

	def __next__(self):
		if len(self.text) - 1 < self.index:
			raise StopIteration

		text = self.text[self.index]
		self.index += 2

		return text


print('-------')
it = Parzyste('kota')
print(next(it))
print(next(it))


# Zad. 8
# Napisz własny iterator, który będzie zwracał tylko samogłoski z przekazanego ciągu tekstowego.
# Zaimplementuj sprawdzanie czy przekazany został string jako argument konstruktora tego iteratora (sprawdź funkcję isinstance()).
class Samogloski:
	def __init__(self, text):
		if not isinstance(text, str):
			pass

		self.samogloski = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y']
		self.text = text
		self.index = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.index > len(self.text) - 1:
			raise StopIteration

		for i in range(self.index, len(self.text)):
			if self.text[i] in self.samogloski:
				self.index = i + 1
				return self.text[i]


print('-------')
for litera in Samogloski('ala ma kota'):
	print(litera)


# Zad. 9
# Przepisz jeden z napisanych przez siebie iteratorów na generator.
def gener(text):
	for i in range(len(text)):
		if i % 2 == 0:
			yield text[i]


print('-------')
gen = gener('kota')
print(next(gen))
print(next(gen))

# Zad. 10
# Zaimportuj pakiet itertools i znajdź w jego dokumentacji sposób na wygenerowanie kombinacji 3 elementowych
# bez powtórzeń na zbiorze 10 elementowym.
import itertools

t = list(itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(t)


# Zad. 11
# Napisz generator, który będzie zwracał kolejne wartości ciągu Fibonacciego.
def fib(n):
	a = 0
	b = 1

	for i in range(n):
		oa = a
		a = b
		b += oa

		yield a


gen = fib(100)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# Zad. 12
# Za pomocą wyrażenia generującego stwórz generator zwracający polskie nazwy miesięcy.

def miesiace():
	for name in ['Styczeń',
			  'Luty',
			  'Marzec',
			  'Kwiecień',
			  'Maj',
			  'Czerwiec',
			  'Lipiec',
			  'Sierpień',
			  'Wrzesień',
			  'Październik',
			  'Listopad',
			  'Grudzień']:
		yield name

gen = miesiace()
print(next(gen))
print(next(gen))
print(next(gen))