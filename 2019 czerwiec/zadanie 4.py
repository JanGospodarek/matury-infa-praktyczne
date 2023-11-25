import math

f_liczby = open('./MIN-R2A1P-193_dane/liczby.txt')
liczby = f_liczby.read().strip().split('\n')
f_pierwszwe = open('./MIN-R2A1P-193_dane/pierwsze.txt')
pierwsze = f_pierwszwe.read().strip().split('\n')


def czy_pierwsza(n):
    if n == 1:
        return False
    for i in range(2, math.ceil(n / 2) + 1):
        if n % i == 0:
            return False
    return True


def zad1():
    ls = []
    for liczba in liczby:
        liczba = int(liczba)
        if liczba >= 100 and liczba <= 5000 and czy_pierwsza(liczba):
            ls.append(liczba)
    with open('./wyniki4_1.txt', 'wt', encoding='UTF-8') as f:
        for l in ls:
            f.write(f'{str(l)} ')


zad1()


def zad2():
    ls = []
    for liczba in pierwsze:
        rev = list(liczba)[::-1]
        rev_liczba = int("".join(rev))
        if czy_pierwsza(rev_liczba):
            ls.append(liczba)

    with open('./wyniki4_2.txt', 'wt', encoding='UTF-8') as f:
        for l in ls:
            f.write(f'{str(l)} ')


zad2()


def suma_cyfr(n: str):
    suma = 0
    for cyfra in n:
        suma += int(cyfra)
    return suma


def zad3():
    ile = 0
    for liczba in pierwsze:
        suma = suma_cyfr(liczba)
        while suma // 10 != 0:
            suma = suma_cyfr(str(suma))
        if suma == 1:
            ile += 1

    with open('./wyniki4_3.txt', 'wt', encoding='UTF-8') as f:

        f.write(f'{str(ile)} ')


zad3()
