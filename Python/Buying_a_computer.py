N = int(input())
komputery = []

for i in range(N):
    dane = input().split()
    name, cpu, gpu, disc, ram, price = dane
    computer = {
        'name': name,
        'cpu': int(cpu),
        'gpu': int(gpu),
        'disc': int(disc),
        'ram': int(ram),
        'price': int(price)
    }
    komputery.append(computer)

M = int(input())

for i in range(M):
    wymagania = input().split()
    minimalne_wartosci_parametrow = {}

    for k in wymagania:
        parametr, wartosc = k.split(':')
        minimalne_wartosci_parametrow[parametr] = int(wartosc)

    pasujace_komputery = []

    for komputer in komputery:
        if all(komputer[parametr] >= minimalne_wartosci_parametrow[parametr] for parametr in minimalne_wartosci_parametrow):
            pasujace_komputery.append(komputer)

    najtanszy_komputer = min(pasujace_komputery, key=lambda x: (x['price'], x['name']))
    print(najtanszy_komputer['name'])
