import sys

H,W,X,Y = input().split()
H = int(H)
W = int(W)
X = int(X)
Y = int(Y)
Macierz = []
Wzorzec = []
Podmacierze = []
for i in range(H):
    wiersz = [int(x) for x in input().split()]
    Macierz.append(wiersz)
for j in range(X):
    wiersz1 = [0]*Y
    Wzorzec.append(wiersz1)

wiersze = len(Macierz)
kolumny = len(Macierz[0])
podmacierze = []

for i in range(wiersze):
    for j in range(kolumny):
        for k in range(i + 1, wiersze + 1):
            for l in range(j + 1, kolumny + 1):
                podmacierz = [row[j:l] for row in Macierz[i:k]]
                podmacierze.append(podmacierz)
for h in podmacierze:
    if h == Wzorzec:
        print("True")
        sys.exit()
print("False")