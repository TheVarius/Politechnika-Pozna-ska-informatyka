N = int(input())
macierz = []
wartosci = []
wyniki = []

for i in range(N):
    wiersz = [int(x) for x in input().split()]
    macierz.append(wiersz)

for j in range(N):
    for k in range(N):
        wart = [j+1, k+1]
        if macierz[j][k] == 1:
            wartosci.append(wart)

for i1 in range(len(wartosci) - 1):
    for j1 in range(i1 + 1, len(wartosci)):
        x1, x2 = wartosci[i1][0], wartosci[j1][0]
        y1, y2 = wartosci[i1][1], wartosci[j1][1]
        if x2 % x1 == 0 and y2 % y1 == 0 and j1 != i1:
            wynik = abs(x1 - x2) + abs(y1 - y2)
        else:
            wynik = 1000
        wyniki.append(wynik)
print(min(wyniki))