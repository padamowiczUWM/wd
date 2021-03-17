import random
import math
import datetime

# Zadanie 1
#
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A={1/x: x∈<1,10>}
# B={1, 2, 4, 8,…, }
# C={x: x∈ B i x jest liczbą podzielną przez 4}

A = [1/x for x in range(1, 11)]
B = [2 ** i for i in range(11)]
C = [i for i in B if i % 4 == 0]

# Zadanie 2
# Wygeneruj losowo macierz 4x4 i wykorzystując Python Comprehension zdefiniuj listę, która będzie zawierała tylko elementy znajdujące się na przekątnej.
random.seed()

macierz = [[random.randint(1, 5) for i in range(4)] for j in range(4)]
przekatna = [val[idx] for idx, val in enumerate(macierz)]
print(macierz)
print(przekatna)

# Zadanie 3
#
# Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a wartość - jednostka
# w jakiej się je kupuje (np. sztuki, kg itd.). Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.

shop = dict(
	ziemniaki='kg',
	pasztet='sztuki',
	chleb='sztuki',
	maslo='sztuki',
	mleko='sztuki',
	cukierki='kg'
)

only_sztuki = [key for key, value in shop.items() if value == 'sztuki']

print(only_sztuki)

# Zadanie 4
#
# Zdefiniuj funkcję, która będzie badać monotoniczność funkcji liniowej:
# y = a x + b

def monotonicznosc(a):
	if a > 0:
		return "Funkcja rosnąca"
	elif a < 0:
		return "Funkcja malejąca"

	return "Funkcja stała"

# Zadanie 5
#
# Napisz funkcję, która będzie sprawdzać czy dwie proste są równoległe czy prostopadłe: Proste dane równaniami:
# y=a1x+b1, y=a2x+b2, są równolegle gdy a1=a2 prostopadłe gdy a1a2=-1

def sprawdz_proste(a1, a2):
	if a1 == a2:
		return "Równoległe"
	elif a1 * a2 == -1:
		return "Prostopadłe"

	return False

# Zadanie 6
#
# Zdefiniuj funkcję, która na podstawie równania okręgu w postaci kanonicznej zwróci długość promienia.
# Funkcja ma przyjmować argumenty domyślne: Równanie okręgu dane jest wzorem:
# (x-a)2+(y-b)2=r2 gdzie (a,b) to środek okręgu a r to promień okręgu.


def dl_promienia(x=2, y=0, a=2, b=2):
	return math.sqrt((x - a) ** 2 + (y - b) ** 2)

print(dl_promienia())

# Zadanie 7
#
# Zdefiniuj funkcję, która oblicza długość przeciwprostokątnej, wykorzystując twierdzenie pitagorasa. Proszę podać wartości domyślne dla funkcji

def pitagoras(a=0, b=0):
	return math.sqrt(a ** 2 + b ** 2)

print(pitagoras(3, 4))

# Zadanie 8
#
# Zdefiniuj funkcję, która zwraca sumę dowolnego ciągu arytmetycznego.
# Funkcja niech przyjmuje jako parametry: a1 (wartość początkowa), r (wielkość o ile rosną kolejne elementy)
# i ile_elementów (ile elementów ma sumować). Ponadto funkcja niech przyjmuje wartości domyślne: a1= 1, r=1, ile=10.

def sum_ca(a1=1, r=1, ile_elementow=10):
	return a1 + (r * ile_elementow)

print(sum_ca())

# Zadanie 9
#
# Wykorzystując poprzedni przykład zdefiniuj funkcję, która będzie liczyć iloczyn elementów ciągu.

def ciag(*liczby):
	iloczyn = None
	for liczba in liczby:
		if iloczyn is None:
			iloczyn = liczba
		else:
			iloczyn *= liczba

	if iloczyn is None:
		return 0.0

	return iloczyn

print(ciag(1, 2, 3, 4))

# Zadanie 10
#
# Napisz funkcję, która wykorzystuje symbol **.
# Funkcja ma przyjmować listę zakupów w postaci: klucz to nazwa produktu a wartość to ilość.
# Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać tę wartość.
def ile_produktow(**kwargs):
	return sum([int(value) for value in kwargs.values()])

print(ile_produktow(jabko=2,maslo=5,banany=8))

# Zadanie 11
#
# Stwórz moduł o nazwie dni_tygodnia.py i umieść w nim co najmniej dwie funkcje zwracające polskie
# nazwy dni tygodnia w zależności od przekazanego parametru. Propozycje: funkcja zwracająca dzień tygodnia
# dla dowolnej daty przekazanej jako argument, dzień tygodnia na podstawie numeru dnia tygodnia, funkcja
# zwracająca skrócone nazwy dni tygodnia, funkcja zwracająca słownik par gdzie klucz to dzień miesiąca
# a wartość to polska nazwa dnia tygodnia dla danego miesiąca przekazanego jako argument funkcji (rok, miesiąc zapewne).

import dni_tygodnia as dt

current_date = datetime.datetime.now()

print(dt.date_day(current_date))
print(dt.date_day_short(current_date))
print(dt.month_days_name(current_date))