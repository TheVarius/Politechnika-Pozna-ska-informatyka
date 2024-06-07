import sys

def usun_wiersz(macierz, x, y):
    macierz1 = [row[:] for row in macierz]
    del macierz1[x]
    macierz1 = list(zip(*macierz1))
    del macierz1[y]
    macierz1 = list(zip(*macierz1))
    macierz1 = [list(x) for x in macierz1]

    return macierz1

l = []
macierz = []
wzorzec = []
N = int(input())

for k in range(N):
    wiersz = input().split()
    macierz.append(wiersz)

for g in range(N-1):
    wiersz1 = input().split()
    wzorzec.append(wiersz1)

for i in range(N):
    for j in range(N):
        wynik = usun_wiersz(macierz, i, j)
        if wynik == wzorzec:
            print("True")
            sys.exit()

print("False")
