import numpy as np


# Zadanie 1
# Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.
def zadanie1():
	a = np.linspace(0, np.pi, num=3)
	b = np.arange(3)
	mnozenie = a * b
	print(a, b, mnozenie)


# Zadanie 2
# Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.
def zadanie2():
	c = np.arange(2, 11).reshape(3, 3)
	d = np.arange(1, 17).reshape(4, 4)
	print("Min rzędu: {}\nMin kolumny: {}".format(min(c.min(axis=1)), min(c.min(axis=0))))
	print("Min rzędu: {}\nMin kolumny: {}".format(min(d.min(axis=1)), min(d.min(axis=0))))


# Zadanie 3
# Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.
def zadanie3():
	a = np.linspace(0, np.pi, num=3)
	b = np.arange(3)
	iloczyn = a.dot(b)
	print(iloczyn)


# Zadanie 4
# Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga liczby rzeczywiste.
# Następnie wykonaj na nich operację mnożenia.
def zadanie4():
	e = np.array([1, 2, 3])
	f = np.array([-1, -2, -3])
	print(e * f)


# Zadanie 5
# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.
def zadanie5():
	g = np.arange(6).reshape(2, 3)
	a = np.sin(g)
	print(a)
	return a


# Zadanie 6
# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.
def zadanie6():
	g = np.arange(6).reshape(2, 3)
	b = np.cos(g)
	print(b)
	return b


# Zadanie 7
# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.
def zadanie7():
	c = zadanie5() + zadanie6()
	print(c)


# Zadanie 8
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.
def zadanie8():
	a = np.arange(9).reshape(3, 3)

	for i in a:
		print(i)


# Zadanie 9
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia” macierzy.
def zadanie9():
	a = np.arange(9).reshape(3, 3)

	for i in a.flat:
		print(i)


# Zadanie 10
# Wygeneruj macierz 9x9 a następnie zmień jej kształt.
def zadanie10():
	a = np.arange(81).reshape(9, 9)
	b = a.reshape(27, 3)
	c = a.reshape(3, 27)
	print(b)
	print(c)


# Zadanie 11
# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6.
# Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?
def zadanie11():
	a = np.arange(12)
	b = a.reshape(3, 4)
	c = a.reshape(4, 3)
	d = a.reshape(2, 6)
	e = a.shape
	f = b.shape
	g = c.shape
	h = d.shape

	print(a)
	print(e)
	print(b)
	print(f)
	print(c)
	print(g)
	print(d)
	print(h)


# zadanie11()
