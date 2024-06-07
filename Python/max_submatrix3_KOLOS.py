def Checker(matrix):
    pattern = matrix[0][0]
    a = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == pattern:
                a += 1
    if a == len(matrix) * len(matrix[0]):
        return True
    return False
N = int(input())
macierz = []
list = []
for i in range(N):
    wiersz = [int(x) for x in input().split()]
    macierz.append(wiersz)
for i in range(len(macierz)):
    for j in range(len(macierz[0])):
        for k in range(i+1,len(macierz)+1):
            for l in range(j+1,len(macierz[0])+1):
                submatrice = [row[j:l] for row in macierz[i:k]]
                if Checker(submatrice):
                    list.append(len(submatrice)*len(submatrice[0]))
print(max(list))