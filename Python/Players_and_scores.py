N = int(input())
slownik = {}
for i in range(N):
    wynik1 = 0
    wynik2 = 0
    wyniki = input().replace(' ', ':')
    imie1, wynik1, imie2, wynik2 = wyniki.split(":")
    wynik1, wynik2 = int(wynik1), int(wynik2)
    if imie1 not in slownik.keys():
        slownik[imie1] = [0, 0]
    if imie2 not in slownik.keys():
        slownik[imie2] = [0, 0]
    if wynik1 > wynik2:
        slownik[imie1][0] += 1
    if wynik1 < wynik2:
        slownik[imie2][0] += 1
    slownik[imie1][1] += int(wynik1)
    slownik[imie2][1] += int(wynik2)

sorted_slownik = dict(sorted(slownik.items(), key=lambda x: (-x[1][0], -x[1][1], x[0], reversed == True)))

for slowo in sorted_slownik.keys():
    print(slowo)
