import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data

def randrange(n, vmin, vmax):
		'''
		Funkcja wspomagająca może tworzyć macierz losowych liczb o
		kształcie(n, )
		'''
		return (vmax - vmin) * np.random.rand(n) + vmin

# Zadanie 1
# Wygeneruj wykres liniowy dla z od 0 do 2pi, x = sin(z), y = 2cos(z).
def zadanie1():
	fig = plt.figure()
	ax = fig.gca(projection='3d')

	t = np.linspace(0, 2 * np.pi, 100)
	z = t
	x = np.sin(z)
	y = 2 * np.cos(z)
	ax.plot(x, y, z, label='zadanie 1')
	ax.legend()
	plt.show()


# zadanie1()

# Zadanie 2
# Wygeneruj wykres punktowy dla 5 różnych losowych serii z użyciem różnych znaczników i kolorów: https://matplotlib.org/api/markers_api.html
def zadanie2():
	np.random.seed(19680801)

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	n = 100

	# Dla każdego zbioru styli i zakresów wygeneruj n losowych punktów
	# zdefiniowane przez x z [23, 32], y in [0, 100], z z [zlow, zhigh].
	for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5), ('g', '1', -10, -45), ('y', 'X', -54, -5),
							  ('c', 'd', -84, -54)]:
		xs = randrange(n, 23, 32)
		ys = randrange(n, 0, 100)
		zs = randrange(n, zlow, zhigh)
		ax.scatter(xs, ys, zs, c=c, marker=m)

	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')
	plt.show()


# zadanie2()

# Zadanie 3
# Wygeneruj wykres z przykładu 3 w 5 różnych kolorystkach: https://matplotlib.org/examples/color/colormaps_reference.html
def zadanie3():
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	# generuj dane.
	X = np.arange(-5, 5, 0.25)
	Y = np.arange(-5, 5, 0.25)
	X, Y = np.meshgrid(X, Y)
	R = np.sqrt(X ** 2 + Y ** 2)
	Z = np.sin(R)
	# rysuj powierzchnię.
	surf = ax.plot_surface(X, Y, Z, cmap=cm.jet,
						   linewidth=0, antialiased=False)
	ax.set_zlim(-1.01, 1.01)
	ax.zaxis.set_major_locator(LinearLocator(10))
	ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
	# Dodanie paska kolorów.
	fig.colorbar(surf, shrink=0.5, aspect=5)
	plt.show()


# zadanie3()

# Zadanie 4
# Wygeneruj z pomocą dokumentacji wykres słupkowy z przykładu 4 wykorzystując 5 różnych kombinacji wyglądu.
def zadanie4():
	fig = plt.figure(figsize=(8, 3))
	ax1 = fig.add_subplot(151, projection='3d')
	ax2 = fig.add_subplot(152, projection='3d')
	ax3 = fig.add_subplot(153, projection='3d')
	ax4 = fig.add_subplot(154, projection='3d')
	ax5 = fig.add_subplot(155, projection='3d')
	# fikcyjne dane
	_x = np.arange(4)
	_y = np.arange(5)
	_xx, _yy = np.meshgrid(_x, _y)
	x, y = _xx.ravel(), _yy.ravel()
	top = x + y
	bottom = np.zeros_like(top)
	width = depth = 1
	ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
	ax1.set_title('Wykres zacieniony')
	ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
	ax2.set_title('Wykres nie zacieniony')
	ax3.bar3d(x, y, bottom, width, depth, top, shade=True, lightsource=cm.colors.LightSource(315, 45))
	ax3.set_title('Wykres zacieniony z źródłem światła')
	ax4.bar3d(x, y, bottom, width, depth, top, color='r')
	ax4.set_title('Wykres czerwony')
	ax5.bar3d(x, y, bottom, width, depth, top, color='r', lightsource=cm.colors.LightSource(315, 45))
	ax5.set_title('Wykres czerwony z źródłem światła')

	plt.show()


# zadanie4()

# Zadanie 5
# W przykładzie 3 zmień gęstość próbek do wykresu na krok 0.1 oraz włącz antyaliasing. Wyświetl pierwotny i nowy wykres obok siebie.
def zadanie5():
	fig = plt.figure()
	ax1 = fig.add_subplot(121, projection='3d')
	ax2 = fig.add_subplot(122, projection='3d')
	# generuj dane.
	X = np.arange(-5, 5, 0.25)
	Y = np.arange(-5, 5, 0.25)
	X, Y = np.meshgrid(X, Y)
	R = np.sqrt(X ** 2 + Y ** 2)
	Z = np.sin(R)
	# rysuj powierzchnię.
	surf = ax1.plot_surface(X, Y, Z, cmap=cm.coolwarm,
							linewidth=0, antialiased=False)

	surf2 = ax2.plot_surface(X, Y, Z, cmap=cm.coolwarm,
							 linewidth=0, antialiased=True)

	ax1.set_zlim(-1.01, 1.01)
	ax1.zaxis.set_major_locator(LinearLocator(10))
	ax1.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

	ax2.set_zlim(-1.01, 1.01)
	ax2.zaxis.set_major_locator(LinearLocator(10))
	ax2.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

	# Dodanie paska kolorów.
	fig.colorbar(surf, shrink=0.1, aspect=5)
	fig.colorbar(surf2, shrink=0.1, aspect=5)
	plt.show()


# zadanie5()

# Zadanie 6
# Wygeneruj 2 wykresy: pierwszy punktowy zawierający 20 punktów, drugi zawierający wykres liniowy składający się z 5 punktów.
def zadanie6():
	fig = plt.figure(figsize=plt.figaspect(0.5))
	n = 20
	ax = fig.add_subplot(1, 2, 1, projection='3d')
	for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
		xs = randrange(n, 23, 32)
		ys = randrange(n, 0, 100)
		zs = randrange(n, zlow, zhigh)
		ax.scatter(xs, ys, zs, c=c, marker=m)

	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')

	ax = fig.add_subplot(1, 2, 2, projection='3d')
	t = np.linspace(0, 2 * np.pi, 6)
	z = t
	x = np.sin(t) * np.cos(t)
	y = np.tan(t)
	ax.plot(x, y, z, label='zadanie 1')
	plt.show()


# zadanie6()

# Zadanie 7
# Połącz 2 wykresy z zadania 5 w jeden. Odpowiednio formatując wykresy spróbuj osiągnąć efekt jakby była to gra Snake,
# w której zielony wąż próbuje zjeść czerwone jabłka
def zadanie7():
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	# generuj dane.
	X = np.arange(-5, 5, 0.25)
	Y = np.arange(-5, 5, 0.25)
	X, Y = np.meshgrid(X, Y)
	R = np.sqrt(X ** 2 + Y ** 2)
	Z = np.sin(R)
	# rysuj powierzchnię.
	surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
							linewidth=0, antialiased=False)

	surf2 = ax.plot_surface(X, Y, Z, cmap=cm.jet,
							 linewidth=0, antialiased=True)

	ax.set_zlim(-1.01, 1.01)
	ax.zaxis.set_major_locator(LinearLocator(10))
	ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

	ax.set_zlim(-1.01, 1.01)
	ax.zaxis.set_major_locator(LinearLocator(10))
	ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

	# Dodanie paska kolorów.
	fig.colorbar(surf, shrink=0.1, aspect=5)
	fig.colorbar(surf2, shrink=0.1, aspect=5)
	ax.view_init(elev=20., azim=-35)
	plt.show()
zadanie7()