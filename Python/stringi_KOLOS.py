N = int(input())
suma = 0
slownik = {}
for i in range(N):
    wiersz = input()
    slownik[wiersz] = []
    for j in range(len(wiersz)):
        for k in range(j,len(wiersz)):
            substring = wiersz[:j] + wiersz[j:k] + wiersz[k+1:]
            if substring not in slownik[wiersz] and len(substring) == len(wiersz) - 1:
                slownik[wiersz].append(substring)
for key in slownik.keys():
    for value in slownik.values():
        for substring in value:
            for x in range(2,100):
                if substring*x == key and len(substring) < len(key) - 1:
                    suma += 1
print(suma)
