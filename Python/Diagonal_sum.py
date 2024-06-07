def max_suma_przekatnej(N, M, matrix):
    przekatne = []
    for i in range(N):
        suma1 = 0
        row, col = i, 0
        while row < N and col < M:
            suma1 += matrix[row][col]
            row += 1
            col += 1
        przekatne.append(suma1)
    for j in range(1, M):
        suma2 = 0
        row, col = 0, j
        while row < N and col < M:
            suma2 += matrix[row][col]
            row += 1
            col += 1
        przekatne.append(suma2)

    return max(przekatne)

n, m = map(int, input().split())
macierz = []
for i in range(n):
    wiersz = [int(x) for x in input().split()]
    macierz.append(wiersz)

macierz_odwrocona = []
for wiersz in macierz:
    wiersz = wiersz[::-1]
    macierz_odwrocona.append(wiersz)

res = max_suma_przekatnej(n, m, macierz)
res_odwrocona = max_suma_przekatnej(n, m, macierz_odwrocona)

print(max(res, res_odwrocona))
