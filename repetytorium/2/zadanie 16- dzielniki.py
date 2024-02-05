f = open('../dane/rozdział 2/pliki/16/liczby16.txt')
lines = f.read().strip().split('\n')


def oblicz_NWD(a, b):
    pom = b
    while b != 0:
        pom = b
        b = a % b
        a = pom
    return a


def sito(n):
    tab = [True] * n

    for i in range(2, n):
        j = i * i
        while j < n:
            tab[j] = False
            j = j + i
    return tab


sito_5000 = sito(5000)


def zad1():
    ile = 0
    for i, line in enumerate(lines):
        for j in range(i + 1, len(lines)):
            line2 = lines[j]
            if oblicz_NWD(int(line), int(line2)) == 1:
                ile += 1
    print(ile)


# zad1()


def zad2():
    for line in lines:
        n = int(line)
        ile_lokalnie = 0
        for i in range(1, n + 1):
            if n % i == 0:
                ile_lokalnie += 1
        if ile_lokalnie == 9:
            print(line)


# zad2()

def zad3():
    for line in lines:
        n = int(line)
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        if suma == n:
            print(line)


zad3()
