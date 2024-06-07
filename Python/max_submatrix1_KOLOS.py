def czy_macierz_jednolita(matrix):
    pierwszy_element = matrix[0][0]

    for wiersz in matrix:
        for element in wiersz:
            if element != pierwszy_element:
                return False

    return True
N = int(input())
macierz = [[int(x) for x in input().split()] for y in range(N)]
res = 0
for i in range(len(macierz)):
    for j in range(len(macierz[0])):
        for k in range(i+1, len(macierz)+1):
            for l in range(j+1, len(macierz[0])+1):
                podmacierz = [row[j:l] for row in macierz[i:k]]
                if czy_macierz_jednolita(podmacierz):
                    x,y = len(podmacierz),len(podmacierz[0])
                    if res < x*y:
                        res = x*y
print(res)
