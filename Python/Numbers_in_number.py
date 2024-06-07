n = input()
zbior = []
def podciagi(k):
    slownik_na_podciagi = {}
    for i in range(len(n)):
        for j in range(i, len(n)):
            substring = n[i:j + 1]
            dlugosc = len(substring)

            if dlugosc not in slownik_na_podciagi:
                slownik_na_podciagi[dlugosc] = [substring]
            else:
                slownik_na_podciagi[dlugosc].append(substring)

    return slownik_na_podciagi.values()

for k in (podciagi(n)):
    zbior.append(k)

for j in zbior:
    j1 = (sorted(j, key=lambda x: (-j.count(x), x), reverse=False))
    print(j1[0])