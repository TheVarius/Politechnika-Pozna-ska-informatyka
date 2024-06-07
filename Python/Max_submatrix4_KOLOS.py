N = int(input())
macierz = [[int(x) for x in input().split()] for y in range(N)]
def Filtr(matrix):
    a = 0
    b = 0
    for wiersz in matrix:
        wiersz1 = set(wiersz)
        if len(wiersz1) == 1:
            a += 1
    for wiersz2 in range(len(matrix)-1):
        if matrix[wiersz2] == matrix[wiersz2+1]:
            b += 1
    if a == len(matrix) and b == len(matrix) -1:
        return True
    return False
result = 0
for i in range(len(macierz)):
    for j in range(len(macierz[0])):
        for k in range(i+1,len(macierz)+1):
            for l in range(j+1,len(macierz[0])+1):
                podmacierz = [row[j:l] for row in macierz[i:k]]
                if Filtr(podmacierz):
                    x = len(podmacierz)
                    y = len(podmacierz[0])
                    if x*y > result:
                        result = x*y
print(result)