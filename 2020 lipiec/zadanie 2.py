import math


def znajdz(p, q):
    rozklad = []
    licznik = p
    mianownik = q
    while licznik != 0:
        n = math.ceil(mianownik / licznik)
        rozklad.append(n)

        mianownik_temp = mianownik

        mianownik = mianownik * n
        licznik = licznik * n

        gora = licznik - mianownik_temp
        licznik = gora
    return rozklad


print(znajdz(4, 5))
