N, M = map(int, input().split())
macierz = []
wiersze = []
kolumny = []

for i in range(N):
    wiersz = [int(x) for x in input().split()]
    macierz.append(wiersz)

for x in range(len(macierz)):
    for i in range(len(macierz[0])):
        if macierz[x][i] == 0:
            kolumny.append(i)

            wiersze.append(x)

for i in wiersze:
    macierz[i] = [0] * M

for j in range(len(macierz)):
    for x in kolumny:
        macierz[j][x] = 0

for i in range(len(macierz)):
    for x in range(M):
        print(macierz[i][x], end=" ")
    print()
