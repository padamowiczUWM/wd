import random

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