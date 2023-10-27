## systemy liczbowe

f = open('../dane/rozdział 2/pliki/13/liczby13.txt')
lines = f.read().strip().split('\n')


## zadanie 1
def dec_to_bin(n: int):
    bins = []
    while n > 0:
        bins.append(n % 2)
        n = n // 2
    return bins[::-1]


def zadanie1():
    ile_liczb = 0
    for liczba in lines:
        bin: list[int] = dec_to_bin(int(liczba))

        liczba_1 = 0
        liczba_0 = 0
        for b in bin:
            if b == 0:
                liczba_0 += 1
            else:
                liczba_1 += 1
        if liczba_1 == liczba_0:
            ile_liczb += 1
    return ile_liczb


print(zadanie1())


# zadanie 2
def dec_to_n(n: int, podstawa: int):
    powyzej_9 = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    liczby = []
    while n > 0:
        reszta = n % podstawa
        if reszta > 9:
            liczby.append(powyzej_9[str(reszta)])
        else:
            liczby.append(str(reszta))
        n = n // podstawa
    return liczby[::-1]


def zadanie2():
    cyfry_5 = {}
    cyfry_7 = {}
    cyfry_13 = {}

    for liczba in lines:
        rep_5 = dec_to_n(int(liczba), 5)
        rep_7 = dec_to_n(int(liczba), 7)
        rep_13 = dec_to_n(int(liczba), 13)
        ile_najw_5 = 0
        ile_najw_7 = 0
        ile_najw_13 = 0
        for cyfra in rep_5:
            if cyfra == '4':
                ile_najw_5 += 1
        for cyfra in rep_7:
            if cyfra == '6':
                ile_najw_7 += 1
        for cyfra in rep_13:
            if cyfra == 'C':
                ile_najw_13 += 1
        cyfry_5[str(liczba)] = ile_najw_5
        cyfry_7[str(liczba)] = ile_najw_7
        cyfry_13[str(liczba)] = ile_najw_13

    print(sorted(cyfry_13.items(), key=lambda x: x[1], reverse=True))


print(zadanie2())


def zadanie3():
    liczby_symetryczne = []
    for liczba in lines:
        rep_16 = dec_to_n(int(liczba), 16)
        czy_symetryczna = True
        for i in range(len(rep_16)):
            if rep_16[i] != rep_16[len(rep_16) - 1 - i]:
                czy_symetryczna = False
        if czy_symetryczna:
            liczby_symetryczne.append(liczba)
    return liczby_symetryczne


print(zadanie3())
