import math

f = open('./DANE/liczby.txt')
lines = f.read().strip().split('\n')


def zad1():
    for liczba in lines:
        odbicie = int(liczba[::-1])
        if odbicie % 17 == 0:
            print(odbicie)


# zad1()

def zad2():
    n = 0
    n_abs = 0
    for liczba in lines:
        odbicie = int(liczba[::-1])
        bezwzgl = math.fabs(int(liczba) - odbicie)
        if bezwzgl > n_abs:
            n_abs = bezwzgl
            n = liczba
    print(n, n_abs)


# zad2()

def czy_pierwsza(n: int):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def zad3():
    for liczba in lines:
        odbicie = int(liczba[::-1])
        if czy_pierwsza(odbicie) and czy_pierwsza(int(liczba)):
            print(liczba)


# zad3()


def zad4():
    dict = {}
    for liczba in lines:
        if liczba in dict.keys():
            dict[liczba] += 1
        else:
            dict[liczba] = 1
    #     Różne
    print(len(dict.keys()))
    ile_2 = 0
    ile_3 = 0
    for key in dict.keys():
        if dict[key] == 2:
            ile_2 += 1
        if dict[key] == 3:
            ile_3 += 1
    print(ile_2, ile_3)

# zad4()
