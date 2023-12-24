f = open('./Dane_2205/liczby.txt')
lines = f.read().strip().split('\n')


def zad1():
    ile = 0
    pierwsza = ""
    for line in lines:
        if line[0] == line[-1]:
            ile += 1
            if pierwsza == "":
                pierwsza = line
    print(ile, pierwsza)


# zad1()


def rozloz(n: int):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            czynniki.append(k)
        k += 1
    return czynniki


def zad2():
    max_czynnikow = ""
    max_czynnikow_dl = 0
    max_czynnikow_unikalnych = ""
    max_czynnikow_unikalnych_dl = 0

    for line in lines:
        czynniki = rozloz(int(line))
        set_czynniki = set(czynniki)
        if len(czynniki) > max_czynnikow_dl:
            max_czynnikow = line
            max_czynnikow_dl = len(czynniki)
        if len(set_czynniki) > max_czynnikow_unikalnych_dl:
            max_czynnikow_unikalnych = line
            max_czynnikow_unikalnych_dl = len(set_czynniki)
    print(max_czynnikow, max_czynnikow_dl, max_czynnikow_unikalnych, max_czynnikow_unikalnych_dl)


# zad2()
f_trojki = open('./trojki.txt', "w", encoding="UTF-8")


def zad3():
    trojki = []
    for line1 in lines:
        liczba1 = int(line1)
        for line2 in lines:
            liczba2 = int(line2)
            if liczba2 % liczba1 == 0 and liczba2 != liczba1:
                for line3 in lines:
                    liczba3 = int(line3)
                    if liczba3 % liczba2 == 0 and liczba3 != liczba1 and liczba3 != liczba2:
                        trojki.append([liczba1, liczba2, liczba3])
                        f_trojki.write(f'{line1} {line2} {line3} \n')
    f_trojki.close()
    ile = 0
    for line1 in lines:
        liczba1 = int(line1)
        for line2 in lines:
            liczba2 = int(line2)
            if liczba2 % liczba1 == 0 and liczba2 != liczba1:
                for line3 in lines:
                    liczba3 = int(line3)
                    if liczba3 % liczba2 == 0 and liczba3 != liczba1 and liczba3 != liczba2:
                        for line4 in lines:
                            liczba4 = int(line4)
                            if liczba4 % liczba3 == 0 and liczba4 != liczba1 and liczba4 != liczba2 and liczba4 != liczba3:
                                for line5 in lines:
                                    liczba5 = int(line5)
                                    if liczba5 % liczba4 == 0 and liczba5 != liczba1 and liczba5 != liczba2 and liczba5 != liczba3 and liczba5 != liczba4:
                                        ile += 1
    print(ile)


zad3()
