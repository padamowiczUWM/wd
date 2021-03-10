import math as m
from datetime import datetime


# Zadanie 1

print(m.e ** 10)
print(m.pow(m.log(5 + m.sin(8) ** 2), 1.0/6.0))
print(m.floor(3.55))
print(m.ceil(3.80))


# Zadanie 2
imie2 = "PATRYK"
nazwisko = "ADAMOWICZ"
print("%s %s" % (imie2.capitalize(), nazwisko.capitalize()))


# Zadanie 3
text = "la la la"
print(text.count('la'))


# Zadanie 4
el_index = "COŚ TAM"
print("Druga: %s, ostatnia %s" % (el_index[1], el_index[-1]))


# Zadanie 5 i 6
lorem = """Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym.
Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki.
Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym.
Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum,
a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków
na komputerach osobistych, jak Aldus PageMaker"""

podzial = lorem.split(" ")


# Zadanie 7
litera_1 = imie2[2]
litera_2 = nazwisko[3]

print("W tekście jest {liczba_liter1}​​ liter {litera_1}​​ oraz {liczba_liter2}​​ liter {litera_2}​​".format(
   liczba_liter1=imie2.count(litera_1),
   liczba_liter2=nazwisko.count(litera_2),
   litera_1=litera_1,
   litera_2=litera_2
))

# Zadanie 8
data = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format(**data))
print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))
print('{} {}'.format("Patryk", "Adamowicz"))
print('{1} {0}'.format('Adamowicz', 'Patryk'))
print('{:.6}'.format('Patryk Adamowicz'))