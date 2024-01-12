f = open('./Dane_2305/pi.txt')
lines = f.read().strip().split('\n')


def zad1():
    ile = 0
    for i in range(1, len(lines)):
        liczba = int(lines[i - 1] + lines[i])
        if liczba > 90:
            ile += 1
    print(ile)


# zad1()

def zad2():
    d = {}
    for i in range(100):
        d[str(i)] = 0
    for i in range(1, len(lines)):
        liczba = int(lines[i - 1] + lines[i])
        d[str(liczba)] += 1

    min = '0'
    max = '0'
    for key in d.keys():
        if d[key] == d[min]:
            if int(key) < int(min):
                min = key
        if d[key] == d[max]:
            if int(key) < int(max):
                max = key
        if d[key] < d[min]:
            min = key
        if d[key] > d[max]:
            max = key
    print(min, d[min], max, d[max])


# zad2()
def check_malejacy(malejacy):
    for i in range(1, len(malejacy)):
        if not (malejacy[i] < malejacy[i - 1]):
            return False
    return True


def czy_rosnaco_malejacy(tab: list):
    rosnacy = [tab[0]]

    for i in range(1, len(tab)):
        if tab[i] > tab[i - 1]:
            rosnacy.append(tab[i])
        else:
            break

    if len(rosnacy) > len(tab) - 1 or len(rosnacy) < 2:
        return False

    malejacy = tab[len(rosnacy):]
    czy_ciag_jest_malejacy = True
    print(malejacy)

    if malejacy[0] < rosnacy[len(rosnacy) - 1]:
        cp = malejacy
        cp.insert(0, rosnacy[len(rosnacy) - 1])
        czy_ciag_jest_malejacy = check_malejacy(cp)
    else:
        if len(malejacy) < 2:
            return False
        czy_ciag_jest_malejacy = check_malejacy(malejacy)

    # print(rosnacy, malejacy, czy_ciag_jest_malejacy)

    return czy_ciag_jest_malejacy


print(czy_rosnaco_malejacy([1, 2, 3, 4, 5, 4]))


def zad3():
    ile = 0
    ciagi = []
    for i in range(5, len(lines)):
        ciag = [int(lines[i - 5]), int(lines[i - 4]), int(lines[i - 3]), int(lines[i - 2]),
                int(lines[i - 1]), int(lines[i])]
        print(ciag)
        if czy_rosnaco_malejacy(ciag):
            ciagi.append(ciag)
            ile += 1
    print(ile, ciagi)


zad3()


def zad4():
    max_dlugosc = 0
    max_pozycja = 0
    lokalna_dlugosc = 0
    lokalna_pozycja = 0

    for i in range(len(lines) - 5):
        czy_rosnacy = True
        czy_malejacy = True
        poprzednia_liczba = int(lines[i])
        j = i + 1
        while j < len(lines) and (czy_rosnacy or czy_malejacy):
            lokalna_dlugosc += 1
            obecna_liczba = int(lines[j])
            if czy_rosnacy and obecna_liczba <= poprzednia_liczba:
                if lokalna_dlugosc == 1:
                    lokalna_dlugosc = 0
                    break
                czy_rosnacy = False
            elif not czy_rosnacy and czy_malejacy and obecna_liczba >= poprzednia_liczba:
                czy_malejacy = False
                if lokalna_dlugosc > max_dlugosc:
                    max_dlugosc = lokalna_dlugosc
                    max_pozycja = i
                lokalna_dlugosc = 0
            poprzednia_liczba = obecna_liczba
            j += 1
    print(max_dlugosc, max_pozycja + 1, lines[max_pozycja:max_pozycja + max_dlugosc])

# zad4()
