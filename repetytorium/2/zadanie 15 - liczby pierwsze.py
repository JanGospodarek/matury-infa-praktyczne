import math

f = open('../dane/rozdział 2/pliki/15/liczby15.txt')
lines = f.read().strip().split('\n')


## zadanie 1
def czy_p(n):
    if n == 2:
        return True
    for i in range(2, math.ceil(n / 2) + 1):
        if n % i == 0:
            return False
    return True


ile_p = 0
for liczba in lines:
    liczba = int(liczba)
    if czy_p(liczba):
        ile_p += 1
print(ile_p)


## zadanie 2
def dec_to_bin(n):
    bin = []
    while n > 0:
        bin.append(n % 2)
        n = n // 2
    return bin[::-1]


liczby_b = []
for liczba in lines:
    suma_cyfr = 0
    suma_bin_cyfr = 0
    for l in liczba:
        suma_cyfr += int(l)
    liczba = int(liczba)
    bin = dec_to_bin(liczba)
    for l in bin:
        suma_bin_cyfr += l
    if czy_p(liczba) and czy_p(suma_cyfr) and czy_p(suma_bin_cyfr):
        liczby_b.append(liczba)
print(sorted(liczby_b))
## zadanie 3
liczby_p = []
for liczba in lines:
    if czy_p(int(liczba)):
        liczby_p.append(int(liczba))
pary = []
s_liczby_p = sorted(liczby_p)
for i in range(len(liczby_p)):
    liczba = s_liczby_p[i]
    for l in range(i + 1, len(liczby_p)):
        if s_liczby_p[l] + 2 == liczba or s_liczby_p[l] - 2 == liczba:
            pary.append([liczba, s_liczby_p[l]])

print(pary)