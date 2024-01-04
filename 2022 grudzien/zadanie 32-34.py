f = open('./Dane_2212/liczby.txt')
lines = f.read().strip().split('\n')
import math


def czy_pierwsza(n: int):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def zad1():
    ile = 0
    for liczba in lines:
        liczba = int(liczba)
        if czy_pierwsza(liczba - 1):
            ile += 1
    print(ile)


# zad1()

sito = [True] * 1000001
sito[0] = False
sito[1] = False
for i in range(2, 1000000):
    if sito[i]:
        for j in range(i * i, 1000000, i):
            sito[j] = False
# print(sito[0:100])

pierwsze = []

for i in range(len(sito)):
    if sito[i]:
        pierwsze.append(i)


def zad2():
    najw_rozkladow = 0
    najw_liczba = 0
    najmn_rozkladow = 0
    najmn_liczba = 0
    for l in range(len(lines)):
        liczba = int(lines[l])
        ile_par = 0

        if liczba % 2 == 0:

            a = 2
            b = liczba - a
            while a <= b:
                if sito[a] and sito[b]:
                    ile_par += 1
                a += 1
                b = liczba - a

            if ile_par > najw_rozkladow:
                najw_rozkladow = ile_par
                najw_liczba = liczba
            if najmn_rozkladow == 0 or ile_par < najmn_rozkladow:
                najmn_rozkladow = ile_par
                najmn_liczba = liczba
        print(l)
    print(najw_liczba, najw_rozkladow, najmn_liczba, najmn_rozkladow)


# zad2()


def dec_to_16(n: int):
    A = []
    letters = "ABCDEF"
    while n > 0:
        reszta = n % 16
        if reszta > 9:
            reszta = letters[reszta - 10]
        A.append(str(reszta))
        n //= 16
    return A[::-1]


print(dec_to_16(123))


def zad3():
    hexes = {

    }
    for liczba in lines:
        liczba = int(liczba)
        hex = dec_to_16(liczba)
        for letter in hex:
            if letter in hexes.keys():
                hexes[letter] += 1
            else:
                hexes[letter] = 1
    print(hexes)


zad3()