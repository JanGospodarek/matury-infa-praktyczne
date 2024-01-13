f = open('./DANE/DANE_E/anagram.txt')
lines = f.read().strip().split('\n')
import math


def zad1():
    ile_zrown = 0
    ile_prawie_zrown = 0
    for liczba in lines:
        liczba_1 = liczba.count('1')
        liczba_0 = liczba.count('0')
        if liczba_0 == liczba_1:
            ile_zrown += 1
        if math.fabs(liczba_1 - liczba_0) == 1:
            ile_prawie_zrown += 1
    print(ile_zrown, ile_prawie_zrown)


zad1()
data = []


def Permute(string):
    if len(string) == 0:
        return ['']
    prevList = Permute(string[1:len(string)])
    nextList = []
    for i in range(0, len(prevList)):
        for j in range(0, len(string)):
            newString = prevList[i][0:j] + string[0] + prevList[i][j:len(string)]
            if newString not in nextList:
                nextList.append(newString)
    return nextList


print(Permute('1100'))


def zad2():
    d = {}
    for liczba in lines:
        if len(liczba) == 8:
            permutacje = Permute(liczba[1:])
            d[liczba] = len(permutacje)
    max = 0
    for key in d.keys():
        if d[key] > max:
            max = d[key]
    for key in d.keys():
        if d[key] == max:
            print(key)


# zad2()

def bin_to_dec(bin: str):
    k = 0
    suma = 0
    for i in range(len(bin) - 1, -1, -1):
        suma += int(bin[i]) * 2 ** k
        k += 1
    return suma


def dec_to_bin(dec: int):
    bin = ''
    while dec > 0:
        bin += str(dec % 2)
        dec = dec // 2
    return bin[::-1]


def zad3():
    max_r = 0
    for i in range(1, len(lines)):
        roznica = math.fabs(bin_to_dec(lines[i - 1]) - bin_to_dec(lines[i]))
        if roznica > max_r:
            max_r = roznica
    print(dec_to_bin(int(max_r)))


# print(zad3())

def zad4():
    ile_bez_0 = 0
    max_s = 0
    max_l = ''

    for i in range(len(lines) - 1, -1, -1):
        liczba = lines[i]
        dec = str(bin_to_dec(liczba))
        if dec.count('0') == 0:
            ile_bez_0 += 1
        set_dec = set(list(dec))
        suma_cyfr = 0
        for cyfra in set_dec:
            suma_cyfr += int(cyfra)
        if suma_cyfr >= max_s:
            max_s = suma_cyfr
            max_l = dec
    print(ile_bez_0, max_l)


zad4()
