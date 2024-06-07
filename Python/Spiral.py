n = int(input())
macierz = []
wynik = []
for i in range(n):
    macierz.append([int(x) for x in input().split()])

while macierz:
    cyfry = macierz.pop(0)
    wynik.extend(cyfry)

    if macierz:
        for wiersz in macierz:
            wynik.append(wiersz.pop())

    if macierz:
        cyfry = macierz.pop()[::-1]
        wynik.extend(cyfry)

    if macierz:
        for wiersz in macierz[::-1]:
            wynik.append(wiersz.pop(0))

for x in range(len(wynik)):
    print(wynik[x], end=" ")