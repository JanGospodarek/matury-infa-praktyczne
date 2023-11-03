import math

f = open('../dane/rozdział 2/pliki/14/liczby14.txt')
lines = f.read().strip().split('\n')
print(lines)
ile_fib = 0
for liczba in lines:
    liczba = int(liczba)
    n1 = 0
    n2 = 1
    cur = 1
    if liczba == 0 or liczba == 1:
        ile_fib += 1
    else:
        while n2 <= liczba:
            cur = n2
            temp = n2
            n2 = n2 + n1
            n1 = temp
        if cur == liczba:
            ile_fib += 1
print(ile_fib)

kat_1 = []
kat_2 = []
kat_3 = []
for liczba in lines:
    liczba = int(liczba)
    n1 = 0
    n2 = 1
    cur = 1

    while n2 <= liczba + 3:
        cur = n2
        temp = n2
        n2 = n2 + n1
        n1 = temp
        if cur + 1 == liczba or cur - 1 == liczba:
            kat_1.append(liczba)
        if cur + 2 == liczba or cur - 2 == liczba:
            kat_2.append(liczba)
        if cur + 3 == liczba or cur - 3 == liczba:
            kat_3.append(liczba)
s_kat_1 = sorted(list(set(kat_1)))
s_kat_2 = sorted(list(set(kat_2)))
s_kat_3 = sorted(list(set(kat_3)))
print(s_kat_2)

l = []


def cz_p(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(n / 2) + 1):
        if n % i == 0:
            return False
    return True


print(cz_p(23))

for liczba in lines:
    liczba = int(liczba)
    n1 = 0
    n2 = 1
    cur = 1

    while n2 <= liczba + 3:
        cur = n2
        temp = n2
        n2 = n2 + n1
        n1 = temp
        if cur == liczba and cz_p(liczba):
            l.append(liczba)
print(sorted(l))
