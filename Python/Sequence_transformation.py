N, M = input().split()
N = int(N)
M = int(M)
S = input()
S1 = S
l = []
l1 = []
for i in range(M):
    zamiana = input()
    liczba1, liczba2, wzor = zamiana.split(';')
    liczba1 = int(liczba1)
    liczba2 = int(liczba2)
    S = S[:min(liczba1, liczba2)] + wzor + S[max(liczba1, liczba2) + 1:]
    l.append(S)

for i in range(len(l)):
    x = len(l[i])
    l1.append(x)

max_dlugosc = max(l1)
index = l1.index(max_dlugosc)

if len(l[index]) > len(S1):
    print(S)
    print(l[index])
else:
    print(S)
    print(S1)