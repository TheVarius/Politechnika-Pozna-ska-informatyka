n,m = input().split()
n = int(n)
m = int(m)
macierz = []
macierz1 = []
macierz2 = []

for x in range(n):
    a = input().split()
    a1 = [int(x) for x in a]
    macierz.append(a1)

for i in range(len(macierz)):
    for j in range(m):
        macierz1.append(macierz[i][j])
macierz1_sorted = sorted(macierz1)

while macierz1_sorted:
    macierze, macierz1_sorted = macierz1_sorted[:n], macierz1_sorted[n:]
    macierz2.append(macierze)
for w in range(n):
    for z in range(len(macierz2)):
        print(macierz2[z][w], end = " ")
    print("")