def najmniejszy_w_wierszu(matrix, x):
    return matrix[x].index(min(matrix[x]))

def najmniejszy_w_kolumnie(matrix, y):
    transponowana_macierz = list(map(list, zip(*matrix)))
    return najmniejszy_w_wierszu(transponowana_macierz, y)

def minimum_w_wierszu(matrix, x):
    return min(matrix[x])

def minimum_w_kolumnie(matrix, y):
    transponowana_macierz = list(map(list, zip(*matrix)))
    return minimum_w_wierszu(transponowana_macierz, y)

n = int(input())
a = input().split()
x = int(a[0])
y = int(a[1])
macierz = []

for i in range(n):
    wiersz = [int(x) for x in input().split()]
    macierz.append(wiersz)

while True:
    if minimum_w_wierszu(macierz, x) < macierz[x][y]:
        y = najmniejszy_w_wierszu(macierz, x)
    elif minimum_w_kolumnie(macierz, y) < macierz[x][y]:
        x = najmniejszy_w_kolumnie(macierz, y)
    else:
        break

print(x, y)