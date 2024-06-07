import sys
n = input().lower()
l1 = []
l2 = []
for x in range(len(n)):
    for i in range(x, len(n)):
        substring = n[:x] + n[x+1:i] + n[i+1:]
        if len(substring) > 0:
            l1.append(substring)
for wyraz in l1:
    wyraz = wyraz[::-1]
    l2.append(wyraz)
for wyraz1 in range(len(l1)):
    if l1[wyraz1] == l2[wyraz1]:
        print("YES")
        sys.exit()
print("NO")