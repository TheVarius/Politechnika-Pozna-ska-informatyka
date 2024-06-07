N, M, oczekiwane_zwyciestwa = map(int, input().split())
slownik_na_druzyny_i_winy = {}
slownik_na_liczbe_spotkan = {}
druzyny = []
for i in range(N):
    druzyna = input()
    slownik_na_druzyny_i_winy[druzyna] = [0, 0]

for j in range(M):
    druzyna1, druzyna2, gole1, gole2 = input().split(":")
    gole1, gole2 = int(gole1), int(gole2)

    if gole1 > gole2:
        slownik_na_druzyny_i_winy[druzyna1][0] += 1
    elif gole1 < gole2:
        slownik_na_druzyny_i_winy[druzyna2][0] += 1

    slownik_na_druzyny_i_winy[druzyna1][1] += 1
    slownik_na_druzyny_i_winy[druzyna2][1] += 1

for klucz in slownik_na_druzyny_i_winy.keys():
    brakujace_zwyciestwa = slownik_na_druzyny_i_winy[klucz][0]
    pozostale_mecze = slownik_na_druzyny_i_winy[klucz][1]
    maksymalna_liczba_meczy_do_rozegrania = N - 1
    if oczekiwane_zwyciestwa - brakujace_zwyciestwa <= maksymalna_liczba_meczy_do_rozegrania - pozostale_mecze:
        druzyny.append(klucz)
for slowo in sorted(druzyny):
    print(slowo)