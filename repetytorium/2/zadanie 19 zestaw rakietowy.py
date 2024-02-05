f = open('../dane/rozdział 2/pliki/19/oddzialy.txt')
lines = f.read().strip().split('\n')
import math


def zad1():
    straty = 0
    poza_zasiegiem = 0
    for line in lines:
        X = line.split(' ')[0]
        Y = line.split(' ')[1]
        odl = math.sqrt(int(X) ** 2 + int(Y) ** 2)
        if odl == 1 or odl == 20:
            straty += 25
        if odl < 1 or odl > 20:
            poza_zasiegiem += 1
        if odl > 1 and odl < 20:
            straty += 100
    print(straty, poza_zasiegiem)


zad1()


def zad2():
    max_odl = 0
    for line in lines:
        X = line.split(' ')[0]
        Y = line.split(' ')[1]
        odl = math.sqrt(int(X) ** 2 + int(Y) ** 2)
        if odl > max_odl:
            max_odl = odl
    print(max_odl)


zad2()


def znajdz_straty(x, y):
    straty = 0
    for line in lines:
        X = line.split(' ')[0]
        Y = line.split(' ')[1]
        odl = math.sqrt((x - int(X)) ** 2 + (y - int(Y)) ** 2)
        if odl == 2:
            straty += 25
        if odl < 2:
            straty += 100
    return straty


def zad3():
    max_straty = 0
    max_pkt = []
    for x in range(-20, 21):
        for y in range(-20, 21):
            if x != 0 and y != 0:
                straty = znajdz_straty(x, y)
                if straty > max_straty:
                    max_straty = straty
                    max_pkt = [x, y]
    return max_pkt, max_straty


print(zad3())
# print(math.sqrt(int('10') ** 2 + int('10') ** 2))
