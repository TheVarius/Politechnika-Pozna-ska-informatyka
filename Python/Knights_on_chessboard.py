import sys
sys.setrecursionlimit(10000)

def ataki(i, j, m):
    mozliwe_ataki = 0
    for di, dj in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1)]:
        if 0 <= i + di < len(m) and 0 <= j + dj < len(m) and m[i + di][j + dj] == "s":
            mozliwe_ataki += 1
    return mozliwe_ataki

n = int(input())
M = [list(input()) for i in range(n)]

wynik = 0
for i in range(n):
    for j in range(n):
        if M[i][j] == "s":
            wynik += ataki(i, j, M)
print(wynik)
