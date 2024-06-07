n, m = input().split()
n = int(n)
m = int(m)
l = []
kolumny = []
kolumny_posortowane = []
for x in range(m):
    a = input().split()
    l.append(a)

for i in range(n):
    kolumna = []
    for j in range(m):
        l[j][i] = int(l[j][i])
        kolumna.append(l[j][i])
    kolumny.append(kolumna)

for g in range(len(kolumny)):
    kolumny[g] = sorted(kolumny[g])
    kolumny_posortowane.append(kolumny[g])

for w in range(n - (n - m)):
    for z in range(len(kolumny_posortowane)):
        print(kolumny_posortowane[z][w], end=" ")
    print("")