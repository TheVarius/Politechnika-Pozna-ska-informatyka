def sum_T(matrix):
    suma_kolumny = 0
    for i in range(1,len(matrix)):
        suma_kolumny += matrix[i][len(matrix)//2]
    return sum(matrix[0]) + suma_kolumny
def cross_sum(matrix):
    macierz1 = []
    przekatna1 = 0
    przekatna2 = 0
    for i1 in range(len(matrix)):
        przekatna1 += matrix[i1][i1]
    for wiersz in matrix:
        macierz1.append(wiersz[::-1])
    for x1 in range(len(macierz1)):
        przekatna2 += macierz1[x1][x1]
    return przekatna1 + przekatna2 - matrix[len(matrix)//2][len(matrix)//2]
N = int(input())
macierz = [[int(x) for x in input().split()] for y in range(N)]
res = 0
for i in range(len(macierz)):
    for j in range(len(macierz[0])):
        for k in range(i + 1, len(macierz) + 1):
            for l in range(j+1, len(macierz[0]) + 1):
                podmacierz = [row[j:l] for row in macierz[i:k]]
                if len(podmacierz) % 2 == 1 and len(podmacierz[0]) % 2 == 1 and len(podmacierz) == len(podmacierz[0]) and sum_T(podmacierz) == cross_sum(podmacierz):
                    dl = len(podmacierz)
                    if dl > res:
                        res = dl
print(res)
