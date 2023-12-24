f = open('./dane.txt')
lines = f.read().strip().split('\n')

trues = []


def czy_lucky(n: int):
    tab = [True] * (n + 1)
    tab.insert(0, False)
    for i in range(2, len(tab)):
        if tab[i]:
            k = 0
            for l in range(1, len(tab)):
                if tab[l]:
                    k += 1
                if k == i:
                    tab[l] = False
                    k = 0

    return tab


trues = czy_lucky(10000)


# print(trues)


def zad1():
    ile = 0
    for liczba in lines:
        liczba = int(liczba)
        if trues[liczba]:
            ile += 1
    return ile


print(zad1())


def zad2():
    dlugosc_max = 1
    dl = 1
    pierwszy_wyr_max = -1

    pierwszy_wyr = -1
    for i in range(1, len(lines)):

        if (not trues[int(lines[i - 1])]) and trues[int(lines[i])]:
            pierwszy_wyr = lines[i]

        if trues[int(lines[i - 1])] and trues[int(lines[i])]:
            dl += 1

        if dl > dlugosc_max:
            pierwszy_wyr_max = pierwszy_wyr
            dlugosc_max = dl

        if not trues[int(lines[i])]:
            dl = 1
    return dlugosc_max, pierwszy_wyr_max


import math

print(zad2())


def czy_prime(n):
    if n == 2:
        return True
    if n == 1 or n == 0:
        return False
    for i in range(2, math.ceil(n / 2) + 1):
        if n % i == 0:
            return False
    return True


def zad3():
    ile = 0
    for liczba in lines:
        if trues[int(liczba)] and czy_prime(int(liczba)):
            ile += 1
    print(ile)


zad3()
