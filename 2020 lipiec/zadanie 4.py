f = open('./DANE/identyfikator.txt')
lines = f.read().strip().split('\n')


def zad1():
    suma = 0
    ids = []
    for identyfikator in lines:
        numery = list(identyfikator[3:])
        s = 0
        for numer in numery:
            s += int(numer)
        if s == suma:
            ids.append(identyfikator)
        elif s > suma:
            ids = [identyfikator]
            suma = s
    with open('./wyniki4_1.txt', 'wt', encoding='UTF-8') as wyn:
        for id in ids:
            wyn.write(f'{id}\n')


# zad1()

def czy_palindrom(slowo: str):
    slowo = list(slowo)
    for i in range(len(slowo) // 2 + 1):
        if slowo[i] != slowo[len(slowo) - 1 - i]:
            return False
    return True


def zad2():
    with open('./wyniki4_2.txt', 'wt', encoding="UTF-8") as wyn:
        for id in lines:
            if czy_palindrom(id[:3]) or czy_palindrom(id[3:]):
                wyn.write(f'{id}\n')


# zad2()
def zad3():
    wagi = [7, 3, 1, 7, 3, 1, 7, 3]
    with open('./wyniki4_3.txt', 'wt', encoding="UTF-8") as wyn:
        for id in lines:
            seria = id[:3]
            cyfra_kontrolna = id[3]
            identyfikator = id[4:]
            kod = list(seria + identyfikator)
            suma = 0
            for i, znak in enumerate(kod):
                waga = wagi[i]
                wartosc = 0
                if i < 3:
                    wartosc = ord(znak) - 55
                else:
                    wartosc = int(znak)
                suma += waga * wartosc
            if int(cyfra_kontrolna) != suma % 10:
                wyn.write(f'{id}\n')


zad3()
