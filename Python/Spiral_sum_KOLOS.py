n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
results = []

while matrix:
    suma = 0
    suma += sum(matrix.pop(0))
    if matrix and matrix[0]:
        for row in matrix:
            suma += row.pop()
    if matrix:
        suma += sum(matrix.pop())
    if matrix and matrix[0]:
        for row in matrix:
            suma += row.pop(0)
    results.append(suma)

for rows in results:
    print(rows)