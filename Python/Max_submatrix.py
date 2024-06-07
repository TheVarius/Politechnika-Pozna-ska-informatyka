def Transpose(M):
    macierz_T = []
    for j in range(len(M[0])):
        tmp = []
        for k in range(len(M)):
            tmp.append(M[k][j])
        macierz_T.append(tmp)
    return macierz_T

def cross_sum(M1):
    a = 0
    m = Transpose(M1)
    for i in range(len(M1)):
        tmp = sum(M1[i]) * sum(m[i])
        a += tmp
    return a

N,n = input().split()
N = int(N)
n = int(n)
macierz = []

wyniki = []
for i in range(N):
    wiersz = [int(x) for x in input().split()]
    macierz.append(wiersz)

wiersze = len(macierz)
kolumny = len(macierz[0])
podmacierze = []

for i in range(wiersze):
    for j in range(kolumny):
        for k in range(i + 1, wiersze + 1):
            for l in range(j + 1, kolumny + 1):
                podmacierz = [row[j:l] for row in macierz[i:k]]
                podmacierze.append(podmacierz)
podmacierze2 = [podmacierz for podmacierz in podmacierze if len(podmacierz[0]) == n and len(podmacierz) == n]

for k in podmacierze2:
    wyniki.append(cross_sum(k))

print(max(wyniki))
