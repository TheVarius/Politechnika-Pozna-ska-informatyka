def odleglosci(matrix, x, y, a):
    l = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > a:
                distance = abs(x - i) + abs(y - j)
                l.append(distance)

    if len(l) == 0:
        return -1
    else:
        return min(l)

N = int(input())
macierz = []

for i in range(N):
    wiersz = [int(x) for x in input().split()]
    macierz.append(wiersz)

for i in range(len(macierz)):
    for j in range(len(macierz[0])):
        print(odleglosci(macierz, i, j, macierz[i][j]), end=" ")
    print()

