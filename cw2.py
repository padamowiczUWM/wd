import math

# Zadanie 1
# Napisz skrypt, który pobiera od użytkownika zdanie i liczy w nim spacje. Wynik wyświetla na ekranie (użyj instrukcji input)
user_text = input("Wpisz jakieś zdanie: ")

print(user_text.count(' '))

# Zadanie 4
# Napisz skrypt, który pobiera od użytkownika liczbę i wypisuje na ekran wartość bezwzględną tej liczby

user_number = input("Wpisz jakąś liczbe: ")
print(math.fabs(user_number))

# Zadanie 5
# Napisz skrypt, który pobiera od użytkownika trzy liczby a, b i c. Sprawdza następujące warunki:

# czy a zawiera się w przedziale (0,10>
# oraz czy jednocześnie a>b lub b>c.
# Jeśli warunki są spełnione lub nie to ma się wyświetlić odpowiedni komunikat na ekranie.

user_a = input("Podaj liczbę a:")
user_b = input("Podaj liczbę b:")
user_c = input("Podaj liczbę c:")

if 0 < user_a <= 10 and (user_a > user_b or user_b > user_c):
	print("Warunki są spełnione.")
else:
	print("Warunki nie są spełnione.")

# Zadanie 6
# Napisz pętlę, która wyświetla liczby podzielne przez 5.

nums = [1, 5, 10, 12, 15]

for num in nums:
	if num % 5 == 0:
		print(num)

# Zadanie 7
# Napisz pętle, która pobiera liczby od użytkownika i wyświetla ich kwadraty na ekranie.
for _ in range(10):
	n = input("Podaj liczbe: ")
	print('Kwadrat liczby {n} to {k}'.format(n=n, k=(n ** 2)))

# Zadanie 8
# Napisz skrypt, który odczytuje liczby od użytkownika i umieszcza je na liście. Wykorzystaj pętle while.

lis = list()
while True:
	l = input("Wprowadź liczbe: ")
	lis.append(int(l))


# Zadanie 9
# Napisz skrypt, który odczytuje od użytkownika liczbę wielocyfrową i sumuje jej cyfry. Wynik wyświetla na ekranie. Wykorzystaj pętle while.

big_number = input("Wprowadź liczbe:")

i = 0
suma = 0
while len(big_number) == i:
	suma += int(big_number[i])

print(suma)

# Zadanie 10
# Napisz skrypt, który rysuje wieżę z literek. Użytkownik podaje wysokość wieży ale nie więcej jak 10.

tower_size = None

while tower_size is None or tower_size > 10:
	tower_size = int(input('Wprowadź wielkość wieży (nie więcej jak 10): '))

for i in range(tower_size):
	print("A" * (i + 1))