import math

f = open('./Dane_PR2/pary.txt')
lines = []
for line in f.read().strip().split('\n'):
    t = line.split(' ')
    lines.append(t)


def czy_pierwsza(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(n / 2) + 1):
        if n % i == 0:
            return False
    return True


def zad1():
    for t in lines:
        liczba = int(t[0])
        if liczba % 2 == 0 and liczba > 4:
            para = []
            roznica = -1
            for i in range(2, liczba):
                if czy_pierwsza(i):
                    for l in range(i, liczba):
                        if czy_pierwsza(l) and l + i == liczba:
                            if l - i > roznica:
                                roznica = l - 1
                                para = [i, l]
            if len(para) > 0:
                print(liczba, para[0], para[1])


# zad1()


def zad2():
    for t in lines:
        slowo = list(t[1])
        max_fragment = slowo[-1]
        max_dl = 1

        akt_fragment = slowo[-1]
        akt_dl = 1
        for i in range(len(slowo) - 1, 0, -1):
            if slowo[i - 1] == slowo[i]:
                akt_dl += 1
                akt_fragment += slowo[i - 1]
            else:
                akt_fragment = slowo[i - 1]
                akt_dl = 1
            if akt_dl >= max_dl:
                max_fragment = akt_fragment
                max_dl = akt_dl

        print(max_fragment, max_dl)


# zad2()
def zad3():
    min = []
    for t in lines:
        liczba = int(t[0])
        slowo = t[1]
        if liczba == len(slowo):
            if len(min) != 0:
                if liczba < min[0] or (liczba == min[0] and slowo < min[1]):
                    min = [liczba, slowo]
            else:
                min = [liczba, slowo]
    return min


print(zad3())
