m, n = input().split()
m = int(m)
n = int(n)
macierz = []


def Transpose(M):
    macierz_T = []
    for j in range(len(M[0])):
        tmp = []
        for k in range(len(M)):
            tmp.append(M[k][j])
        macierz_T.append(tmp)
    return macierz_T


def Reverse_Row(M1, a):
    M1[a] = M1[a][::-1]
    return M1


def Reverse_column(M2, b):
    Mac2 = []
    for i in range(len(M2[0])):
        Mac = []
        for x in range(len(M2)):
            Mac.append(M2[x][i])
        Mac2.append(Mac)
    Mac2[b] = Mac2[b][::-1]
    return Transpose(Mac2)


for i in range(m):
    wiersz = [int(x) for x in input().split()]
    macierz.append(wiersz)

ile_razy = int(input())

for i in range(ile_razy):
    l = []
    a = input().split()
    for i in a:
        l.append(i)
    if len(a) == 2:
        if l[0] == "RC":
            macierz = Reverse_column(macierz, int(l[1]))
        if l[0] == "RR":
            macierz = Reverse_Row(macierz, int(l[1]))
    else:
        macierz = Transpose(macierz)

for i in macierz:
    print(' '.join(map(str, i)))