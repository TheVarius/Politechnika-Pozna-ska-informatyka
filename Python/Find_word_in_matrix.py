import sys
n,m = input().split()
n = int(n)
m = int(m)
pattern = input()
reversed_pattern = pattern[::-1]
l = []
b = 0
for x in range(n):
    a = input()
    l.append(a)
for i in range(m):
    slowo = ""
    for j in range(n):
        slowo = slowo + l[j][i]
    l.append(slowo)

for g in l:
    if pattern in g:
        print("YES")
        sys.exit()
    else:
        b += 1
for h in l:
    if reversed_pattern in h:
        print("YES")
        sys.exit()
    else:
        b += 1
if b != 0:
    print("NO")