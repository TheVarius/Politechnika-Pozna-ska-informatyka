N = int(input())
slownik_na_osoby = {}
slownik_na_sprawdziany = {}
for i in range(N):
    wiersz = input().split()
    for wyraz in wiersz:
        if wiersz[0] not in slownik_na_osoby.keys():
            slownik_na_osoby[wiersz[0]] = [0,0]
        if wyraz not in slownik_na_osoby.keys():
            sprawdzian, ocena = wyraz.split(":")
            if sprawdzian not in slownik_na_sprawdziany.keys():
                slownik_na_sprawdziany[sprawdzian] = [0,0]
            slownik_na_sprawdziany[sprawdzian][0] += float(ocena)
            slownik_na_sprawdziany[sprawdzian][1] += 1
            slownik_na_osoby[wiersz[0]][0] += float(ocena)
            slownik_na_osoby[wiersz[0]][1] += 1

for value in slownik_na_osoby.values():
    value[0] = value[0]/value[1]
for value in slownik_na_sprawdziany.values():
    value[0] = value[0]/value[1]

sorted_slownik_na_osoby = dict(sorted(slownik_na_osoby.items()))
sorted_slownik_na_sprawdziany = dict(sorted(slownik_na_sprawdziany.items()))

for key,value in sorted_slownik_na_osoby.items():
    print(key, value[0])

for key,value in sorted_slownik_na_sprawdziany.items():
    print(key, value[0])