f = open('./DANE/napisy.txt')
lines = f.read().strip().split('\n')


def zad1():
    ile = 0
    for line in lines:
        for c in list(line):
            try:
                l = int(c)
                ile += 1
            except:
                ile = ile
    print(ile)


zad1()


def zad2():
    k = 0
    haslo = ""
    for i in range(19, len(lines), 20):
        haslo += lines[i][k]
        k += 1
    print(haslo)


zad2()


def czy_palindrom(tekst):
    for i in range(len(tekst) // 2):
        if tekst[i] != tekst[len(tekst) - 1 - i]:
            return False
    return True


def zad3():
    haslo = ""
    for line in lines:
        dl = len(list(line))
        tekst_dodany_na_koncu = line + line[0]
        tekst_dodany_na_poczatku = line[dl - 1] + line
        if czy_palindrom(tekst_dodany_na_koncu):
            haslo += tekst_dodany_na_koncu[25]
        elif czy_palindrom(tekst_dodany_na_poczatku):
            haslo += tekst_dodany_na_poczatku[25]
    print(haslo)


zad3()


def zad4():
    haslo = ""
    for line in lines:
        liczby = []
        for c in line:
            try:
                l = int(c)
                liczby.append(c)
            except:
                None
        if len(liczby) % 2 == 1 and len(liczby) > 2:
            liczby.pop()
        if len(liczby) > 1:
            print(liczby)
            for i in range(1, len(liczby), 2):
                liczba = int(liczby[i - 1] + liczby[i])
                dl_hasla = len(haslo)
                if dl_hasla > 3 and haslo[dl_hasla - 1] == "X" and haslo[dl_hasla - 2] == "X" and haslo[
                    dl_hasla - 3] == "X":
                    return haslo
                if liczba >= 65 and liczba <= 90:
                    asc = chr(liczba)
                    haslo += asc


print(zad4())
