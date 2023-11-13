import math

f = open('./MIN-DANE-2017/punkty.txt')
lines = f.read().strip().split('\n')
tab: list[list[int]] = []
for line in lines:
    t = line.split(' ')
    for i in range(2):
        t[i] = int(t[i])
    tab.append(t)


def czy_Pierwsza(n: int):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(n / 2)):
        if n % i == 0:
            return False
    return True


## zadanie 1
def zad1():
    ile_pkt = 0
    for para in tab:
        if czy_Pierwsza(para[0]) and czy_Pierwsza(para[1]):
            ile_pkt += 1
    return ile_pkt


# print(zad1())


## zadnaie 2

def zad2():
    ile_pkt = 0
    for para in tab:
        czy_cyfropodobna = True
        liczby_1 = set(list(str(para[0])))
        liczby_2 = set(list(str(para[1])))
        for cyfra in liczby_1:
            if cyfra not in liczby_2:
                czy_cyfropodobna = False
        for cyfra in liczby_2:
            if cyfra not in liczby_1:
                czy_cyfropodobna = False
        if czy_cyfropodobna:
            ile_pkt += 1
    return ile_pkt


# print(zad2())

## zadanie 3

def zad3():
    najbardziej_oddalone = (tab[0], tab[1])
    odl_max = math.sqrt((tab[1][0] - tab[0][0]) ** 2 + (tab[1][1] - tab[0][1]) ** 2)
    for i, (x1, y1) in enumerate(tab):
        for l, (x2, y2) in enumerate(tab):
            odl = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if odl > odl_max:
                odl_max = odl
                najbardziej_oddalone = (tab[i], tab[l])
    return najbardziej_oddalone, odl_max


# print(zad3())

def zad4():
    ile_wewnatrz = 0
    ile_na_bokach = 0
    ile_na_zewnatrz = 0
    for i, (x, y) in enumerate(tab):
        if math.fabs(x) < 5000 and math.fabs(y) < 5000:
            ile_wewnatrz += 1
        if math.fabs(x) == 5000 or math.fabs(y) == 5000:
            ile_na_bokach += 1
        if math.fabs(x) > 5000 or math.fabs(y) > 5000:
            ile_na_zewnatrz += 1
    return ile_wewnatrz, ile_na_bokach, ile_na_zewnatrz

# print(zad4())
