def who_will_pass(i, j, m):
    suma_sasiadow = 0
    liczba_sasiadow = 0

    for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1)]:
        ni, nj = i + di, j + dj

        if 0 <= ni < len(m) and 0 <= nj < len(m[0]):
            suma_sasiadow += int(m[ni][nj])
            liczba_sasiadow += 1

    if liczba_sasiadow > 0:
        srednia_sasiadow = suma_sasiadow / liczba_sasiadow
    else:
        srednia_sasiadow = 0

    if srednia_sasiadow >= 3 or int(m[i][j]) >= 3:
        print("1", end=" ")
    else:
        print("0", end=" ")


n = int(input())
M = [list(input().split()) for i in range(n)]

for i in range(n):
    for j in range(len(M[0])):
        who_will_pass(i, j, M)
    print("")
