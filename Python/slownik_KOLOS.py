N = int(input())
slownik = {}
l = []
max1 = 0
min1 = 0

for i in range(N):
    wiersz = input().split()
    nazwa_zmiennej = wiersz[0]

    if wiersz[1] == "=" and nazwa_zmiennej not in slownik.keys():
        slownik[nazwa_zmiennej] = int(wiersz[2])
    elif wiersz[1] == "-=":
        slownik[nazwa_zmiennej] -= int(wiersz[2])
    elif wiersz[1] == "+=":
        slownik[nazwa_zmiennej] += int(wiersz[2])

    wartosc_zmiennej = slownik[nazwa_zmiennej]
    if (wartosc_zmiennej > max1 or wartosc_zmiennej < min1) and nazwa_zmiennej not in l:
        l.append(nazwa_zmiennej)
        max1 = max(slownik.values())
        min1 = min(slownik.values())

sorted_l = sorted(l)
print(sorted_l)
