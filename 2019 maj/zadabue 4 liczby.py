f = open('./Dane_PR/liczby.txt')
lines = f.read().strip().split('\n')


def czy_potega(n, podstawa):
    if n == 1:
        return True
    while n > podstawa:
        n = n / podstawa

    if n == podstawa:
        return True
    return False


def zad1():
    ile_poteg = 0
    for liczba in lines:
        if czy_potega(int(liczba), 3):
            ile_poteg += 1
    return ile_poteg


# print(zad1())

def zad2():
    liczby_rowne = []
    for liczba in lines:
        cyfry = list(liczba)
        suma_silni = 0
        for cyfra in cyfry:
            cyfra = int(cyfra)
            if cyfra == 0 or cyfra == 1:
                suma_silni += 1
            else:
                silnia = 1
                for i in range(1, cyfra + 1):
                    silnia *= i
                suma_silni += silnia
        if suma_silni == int(liczba):
            liczby_rowne.append(liczba)
    return liczby_rowne


# print(zad2())
def znajdz_NWD(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def zad3():
    max_NWD = 0
    max_dlugosc = 0
    max_pierwsza_liczba = ''

    NWD_ciagu = znajdz_NWD(int(lines[0]), int(lines[1]))
    dl_ciagu = 2
    pierwsza_liczba_ciagu = lines[0]

    for i in range(2, len(lines)):
        nwd = znajdz_NWD(NWD_ciagu, int(lines[i]))
        if nwd > 1:
            dl_ciagu += 1
            NWD_ciagu = nwd
        else:
            if dl_ciagu > max_dlugosc:
                max_dlugosc = dl_ciagu
                max_pierwsza_liczba = pierwsza_liczba_ciagu
                max_NWD = NWD_ciagu
            dl_ciagu = 2
            NWD_ciagu = znajdz_NWD(int(lines[i - 1]), int(lines[i]))
            pierwsza_liczba_ciagu = lines[i - 1]

    return max_pierwsza_liczba, max_NWD, max_dlugosc


print(zad3())
