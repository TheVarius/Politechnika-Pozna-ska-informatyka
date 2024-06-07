def sortowanie(matrix):
   sorted_matrix = sorted(matrix[0])
   sorted_matrix1 = sorted(matrix[-1])
   if sorted_matrix == matrix[0] and sorted_matrix1 == matrix[-1]:
       return True
   return False

def Diagonals(matrix):
    diag1 = [matrix[i][i] for i in range(min(len(matrix), len(matrix[0])))]
    matrix1 = matrix[::-1]
    diag2 = [matrix1[i][i] for i in range(min(len(matrix1), len(matrix1[0])))]
    return sorted(diag1) == diag1 and sorted(diag2) == diag2

N = int(input())
macierz = [[int(x) for x in input().split()] for _ in range(N)]

for i in range(len(macierz)):
    for j in range(len(macierz[0])):
        for k in range(i + 1, len(macierz) + 1):
            for l in range(j + 1, len(macierz[0]) + 1):
                    podmacierz = [row[j:l] for row in macierz[i:k]]
                    if Diagonals(podmacierz) and sortowanie(podmacierz):
                        print(podmacierz)
