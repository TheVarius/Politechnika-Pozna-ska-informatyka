def who_will_pass2(matrix, x, y, a):
    suma1 = 0
    suma2 = 0
    k = 0
    d = 0

    for i in matrix[x]:
        if i >= a:
            suma1 += i
            k += 1

    transposed_matrix = list(zip(*matrix))

    for j in transposed_matrix[y]:
        if j >= a:
            suma2 += j
            d += 1

    if k + d > 0:
        suma = (suma1 + suma2 - a) / (k + d - 1)
    else:
        suma = 0
    return int(suma)

N = int(input())
macierz = []

for x in range(N):
    wiersz = [int(y) for y in input().split()]
    macierz.append(wiersz)

for i in range(len(macierz)):
    for j in range(len(macierz[0])):
        if who_will_pass2(macierz, i, j, macierz[i][j]) >= 7 or macierz[i][j] >= 7:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()