f = open('./Dane_PR/liczby.txt')
lines = f.read().strip().split('\n')


def sprawdz(liczba: int):
    while liczba > 1:
        if liczba % 3 == 0:
            liczba = liczba // 3
        else:
            return False
    return True


def zad1():
    ile = 0
    for line in lines:
        liczba = int(line)
        if liczba == 1:
            ile += 1
        else:
            if sprawdz(liczba):
                ile += 1
    print(ile)


zad1()


def silnia(n: int):
    silnia = 1
    if n == 0:
        return silnia
    while n > 1:
        silnia = silnia * n
        n -= 1
    return silnia


def zad2():
    for line in lines:
        liczba = int(line)
        n = liczba
        suma_silni = 0
        while n > 0 and suma_silni <= liczba:
            reszta = n % 10
            n = n // 10
            suma_silni += silnia(reszta)
        if suma_silni == liczba:
            print(liczba)


zad2()

t = [5, 70, 28, 42, 98, 1, 3]


def NWD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def zad3():
    dlugosc_lokalnie = 2
    pierwszy_lokalnie = int(lines[0])
    dlugosc_max = 2
    pierwszy_max = int(lines[0])
    nwd_max = 0

    nwd_ciagu = NWD(int(lines[0]), int(lines[1]))
    for i in range(2, len(lines)):
        a = int(lines[i - 1])
        b = int(lines[i])

        nwd_ciagu = NWD(nwd_ciagu, b)
        if nwd_ciagu > 1:

            dlugosc_lokalnie += 1

            if dlugosc_lokalnie > dlugosc_max:
                dlugosc_max = dlugosc_lokalnie
                nwd_max = nwd_ciagu
                pierwszy_max = pierwszy_lokalnie
        else:
            dlugosc_lokalnie = 2
            nwd_ciagu = NWD(a, b)
            pierwszy_lokalnie = a
    print(dlugosc_max, pierwszy_max, nwd_max)


zad3()
