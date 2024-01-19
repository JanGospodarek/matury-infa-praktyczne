def SumaKwCyfr(n):
    suma = 0
    k = 10
    while n > 0:
        reszta = n % 10
        suma += reszta * reszta
        n = n // 10
    return suma


print(SumaKwCyfr(123))


def znajdz(n):
    i = 0
    T = []
    while n != 1:
        T.append(n)
        n = SumaKwCyfr(n)
        for l in range(i + 1):
            if T[l] == n:
                return False
                break
        i += 1
    return True


print(znajdz(82))
