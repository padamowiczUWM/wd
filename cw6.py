import numpy as np

# Zadanie 1
# Za pomocą funkcji arange stwórz tablicę Numpy składającą się 20 kolejnych wielokrotności liczby 2.
a = np.arange(2, 42, step=2)
print(a)

# Zadanie 2
# Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int64.
b = [2.4, 3.8, 4.5]
c = np.array(b, dtype='int64')
print(c)


# Zadanie 3
# Napisz funkcję, która będzie:
#
# przyjmowała jeden parametr n w postaci liczby całkowitej
# zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1

def kw(n):
	row = n * n
	return np.arange(1, row + 1)


print(kw(5))


# Zadanie 4
# Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji potęgowania
# oraz ilość kolejnych potęg do wygenerowania. Korzystając z funkcji logspace generuj tablicę jednowymiarową
# kolejnych potęg podanej liczby, np. generuj(2,4) -> [2 4 8 16]
def generuj(liczba, ilosc):
	return np.logspace(1, ilosc, ilosc, base=liczba, dtype='int64')


print(generuj(2, 4))


# Zadanie 5
# Napisz funkcję, która:
# na wejściu przyjmuje jeden parametr określający długość wektora,
# na podstawie parametru generuje wektor, ale w kolejności odwróconej (czyli np. dla n=3 =>[3 2 1])
# generuje macierz diagonalną z w/w wektorem jako przekątną
def wek(n):
	return np.diag([a for a in range(n, 0, -1)])


wek(5)


# Zadanie 6
# Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki,
# gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie.
# Jedno z tych słów powinno być wypisane od prawej do lewej.
def wyk():
	z = np.diag(list('schabowy'))
	print(z)


wyk()

# Zadanie 7
# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
#
# [[2 4 6]
#  [4 2 4]
#  [6 4 2]]
diag = np.zeros((3, 3))

for i in range(1, 4):
	x = np.diag([2^i for a in range(3)])
	diag = diag + x

print(diag)

# Zadanie 8
# Napisz funkcję, która:
#
# jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr ‘kierunek’,
# parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
# funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat,
# że ilość wierszy lub kolumn, w zależności od kierunku podziału, nie pozwala na operację)

def func(tab, kierunek='pion'):
	if kierunek == 'poziom':
		first = tab[:int(len(tab) / 2)]
		last = tab[int(len(tab) / 2):]
	else:
		first = tab[:, :int(len(tab)/2)]
		last = tab[:, int(len(tab) / 2):]

	return first, last

nprand = np.random.random_integers(1, 10 + 1, (4, 4))
print(nprand)
print(func(nprand, 'pion'))