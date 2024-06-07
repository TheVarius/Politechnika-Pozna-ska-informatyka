n = input()
l = []
l1 = []
a = 0
for x in range(len(n)):
    for i in range(x, len(n)):
        substring = n[x:i+1]
        if substring[0] == "0":
            continue
        l.append(substring)
for i in l:
    while i[len(i)-1] == "0":
        i = i[:-1]
    l1.append(i)
for j in l1:
    if j == j[::-1]:
        a += 1
print(a)