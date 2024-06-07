def checker(matrix):
    l = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] not in l:
                l.append(matrix[i][j])
    if len(l) == len(matrix) * len(matrix[0]):
        return True
    return False
n = int(input())
res = 0
macierz = [[int(x) for x in input().split()]for y in range(n)]
for i in range(len(macierz)):
    for j in range(len(macierz[0])):
        for k in range(i+1,len(macierz) + 1):
            for g in range(j+1,len(macierz[0]) + 1):
                podmacierz = [row[j:g] for row in macierz[i:k]]
                if checker(podmacierz) and len(podmacierz) * len(podmacierz[0]) > res:
                    res = len(podmacierz) * len(podmacierz[0])
print(res)