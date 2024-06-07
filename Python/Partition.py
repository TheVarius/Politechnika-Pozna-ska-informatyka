n = int(input())
m = [int(x) for x in input().split()]
sublists = []
res2 = []
res3 = []
res = []

for i in range(len(m)):
    for j in range(i, len(m)):
        sublist = m[i:j + 1]
        if len(sublist) > 0:
            suma2 = sum(sublist[0::2])
            suma3 = sum(sublist[0::3])
            res2.append(suma2)
            res3.append(suma3)

for el in res2:
    if el in res3:
        res.append(el)

print(max(res))
