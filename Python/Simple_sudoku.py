macierz = []
macierz_pion = []
macierz_pion2 = []
l = []
l1 = []
l2 = []
l3 = []
a = 0
b = 0
c = 0
liczby = [1,2,3,4,5,6,7,8,9]

for i in range(9):
    wiersz = [int(x) for x in input().split()]
    macierz.append(wiersz)

for z in range(len(macierz)):
    for w in range(9):
        macierz_pion.append(macierz[w][z])

while macierz_pion:
    macierze, macierz_pion = macierz_pion[:(len(wiersz))], macierz_pion[(len(wiersz)):]
    macierz_pion2.append(macierze)

for g in macierz:
    if all(liczba in g for liczba in liczby):
        a += 1

for h in macierz_pion2:
    if all(liczba in h for liczba in liczby):
        b += 1

for x in range(9):
    l.append(macierz[x][x])

for d in macierz:
    d = d[::-1]
    l1.append(d)

for y in range(9):
    l2.append(l1[y][y])

l3.append(l)
l3.append(l2)

for o in l3:
    if all(liczba in o for liczba in liczby):
        c += 1

if a == 9 and b == 9 and c == 2:
    print("X")
if a == 9 and b == 9 and c != 2:
    print("True")
if a != 9 or b != 9:
    print("False")