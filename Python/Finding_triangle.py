n = int(input())
l1 = []
l2 = []
for i in range(n):
    punkty = [int(x) for x in input().split()]
    l1.append(punkty)
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            x1 = l1[j][0] - l1[k][0]
            y1 = l1[j][1] - l1[k][1]
            x2 = l1[i][0] - l1[k][0]
            y2 = l1[i][1] - l1[k][1]
            pole = abs(x1 * y2 - y1 * x2) / 2
            l2.append(pole)
print(min(l2), max(l2))
