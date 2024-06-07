def czy_wiersz(matrix):
    for i in range(len(matrix[0])-1):
        if matrix[0][i] != matrix[0][i+1]:
            return False
    return True
def czy_wiersze(matrix):
    for wiersz in range(len(matrix)-1):
        if matrix[wiersz] != matrix[wiersz+1]:
            return False
    return True

N = int(input())
macierz = [[int(x) for x in input().split()] for y in range(N)]
wynik = 0
for i in range(len(macierz)):
    for j in range(len(macierz[0])):
        for k in range(i+1,len(macierz)+1):
            for l in range(j+1,len(macierz[0])+1):
                podmacierz = [row[j:l] for row in macierz[i:k]]
                if czy_wiersze(podmacierz) and czy_wiersz(podmacierz):
                    if len(podmacierz)*len(podmacierz[0]) > wynik:
                        wynik = len(podmacierz)*len(podmacierz[0])
print(wynik)