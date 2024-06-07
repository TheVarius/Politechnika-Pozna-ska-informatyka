def the_closest_smaller_number(matrix, x, y, a):
    n = len(matrix)
    l = []

    for i in range(n):
        if matrix[x][i] < a:
            distance1 = abs(i - y)
            l1 = [matrix[x][i], distance1]
            l.append(l1)

    for j in range(n):
        if matrix[j][y] < a:
            distance2 = abs(j - x)
            l2 = [matrix[j][y], distance2]
            l.append(l2)

    if not l:
        return -1
    else:
        result = min(l, key=lambda x: (x[1], x[0]))
        return result[0]

N = int(input())
macierz = []

for _ in range(N):
    row = [int(y) for y in input().split()]
    macierz.append(row)

for i in range(N):
    for j in range(N):
        print(the_closest_smaller_number(macierz, i, j, macierz[i][j]), end=" ")
    print()