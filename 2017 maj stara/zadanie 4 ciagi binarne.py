f = open('./Dane_PR/binarne.txt')
lines = f.read().strip().split('\n')


def zad1():
    liczba_dwucyklicznych = 0
    najdluzszy_napis = lines[0]
    for liczba in lines:
        n1 = 0
        n2 = int(len(liczba) / 2)
        czy_dwucykliczna = True
        while n2 < len(liczba):
            if liczba[n2] != liczba[n1]:
                czy_dwucykliczna = False
            n1 += 1
            n2 += 1
        if czy_dwucykliczna:
            liczba_dwucyklicznych += 1
            if len(liczba) > len(najdluzszy_napis):
                najdluzszy_napis = liczba
    return liczba_dwucyklicznych, najdluzszy_napis, len(najdluzszy_napis)


# print(zad1())
def bin_to_dec(bin: str):
    k = 0
    dec = 0
    for i in range(len(bin) - 1, -1, -1):
        dec += int(bin[i]) * 2 ** k
        k += 1
    return dec


def zad2():
    liczba_niepoprawnych = 0
    najkrotszy_napis = lines[0]
    for liczba in lines:
        czy_niepoprawna = False
        for i in range(int(len(liczba) / 4)):
            segment = liczba[i * 4:i * 4 + 4]
            dec = bin_to_dec(segment)
            if dec > 9:
                czy_niepoprawna = True
        if czy_niepoprawna:
            liczba_niepoprawnych += 1
            if len(liczba) < len(najkrotszy_napis):
                najkrotszy_napis = liczba
    return liczba_niepoprawnych, najkrotszy_napis, len(najkrotszy_napis)


# print(zad2())

def zad3():
    najwiekszy_bin = lines[0]
    najwiekszy_dec = bin_to_dec(najwiekszy_bin)
    for liczba in lines:
        dec = bin_to_dec(liczba)
        if dec <= 65535:
            if dec > najwiekszy_dec:
                najwiekszy_bin = liczba
                najwiekszy_dec = dec
    return najwiekszy_bin, najwiekszy_dec

# print(zad3())
