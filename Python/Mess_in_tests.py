def oceny(a):
    imie, ocena = wiersz[0], wiersz[a - 1]
    licznik, mianownik = ocena.split("/")
    ocena = int(licznik) / int(mianownik)
    ocena = round(ocena, 2)
    if 0 < ocena <= 0.49:
        ocena = 2
    if 0.49 < ocena <= 0.69:
        ocena = 3
    if 0.69 < ocena <= 0.89:
        ocena = 4
    if 0.89 < ocena <= 1:
        ocena = 5
    if imie in slownik_na_oceny:
        slownik_na_oceny[imie].append(ocena)
    if imie in slownik_na_imiona:
        slownik_na_oceny[slownik_na_imiona[imie]].append(ocena)
    if imie in slownik_na_inf_indeksy:
        slownik_na_oceny[slownik_na_inf_indeksy[imie]].append(ocena)


N, S = map(int, input().split())
slownik_na_indeksy = {}
slownik_na_oceny = {}
slownik_na_imiona = {}
slownik_na_inf_indeksy = {}
oceny_ostateczne = []
ostateczny_slownik = {}

for i in range(N):
    imie, index = input().split()
    slownik_na_indeksy[imie] = index
    slownik_na_imiona[index] = imie
    slownik_na_inf_indeksy["inf" + index] = imie
    slownik_na_oceny[imie] = []

K = int(input())

for k in range(K):
    wiersz = input().split()
    if len(wiersz) == 2:
        oceny(2)
    elif len(wiersz) == 3:
        oceny(3)

for klucz, wartosci in slownik_na_oceny.items():
    suma_wartosci = sum(wartosci) / S

oceny = list(slownik_na_oceny.values())
lista_uczniow = list(slownik_na_oceny.keys())

for j in oceny:
    ocena = round((sum(j) / S), 2)
    if 0 <= ocena < 3:
        ocena = 2
    if 3 <= ocena < 3.5:
        ocena = 3
    if 3.5 <= ocena < 4.5:
        ocena = 4
    if 4.5 <= ocena <= 5:
        ocena = 5
    oceny_ostateczne.append(ocena)

for i in range(N):
    ostateczny_slownik[lista_uczniow[i]] = oceny_ostateczne[i]

posortowane_klucze = sorted(ostateczny_slownik.keys())
for klucz in posortowane_klucze:
    print(klucz, ostateczny_slownik[klucz])
