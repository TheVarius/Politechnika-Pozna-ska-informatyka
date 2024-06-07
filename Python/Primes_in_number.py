import sys

n = input()
l1 = []
l2 = []


def czy_pierwsza(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


for x in range(len(n)):
    for i in range(x, len(n)):
        if n[x] == "0":
            continue
        substring = n[x:i + 1]
        l1.append(substring)

wszystkie_liczby = [int(i) for i in l1]

for liczba in wszystkie_liczby:
    if czy_pierwsza(liczba) and liczba not in l2:
        l2.append((liczba))

Lexicographic_sort0 = [str(x) for x in l2]
Lexicographic_sort = sorted(Lexicographic_sort0)

Antilexicographic_sort = Lexicographic_sort[::-1]
for i in range(len(Antilexicographic_sort)):
    print(Antilexicographic_sort[i])
